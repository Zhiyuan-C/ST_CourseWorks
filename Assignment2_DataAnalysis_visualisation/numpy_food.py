import numpy as np
import matplotlib.pyplot as plt
import sqlite3


# Get data from dtabase
def get_data(sql:str)->iter:
  # Connect database
  conn = sqlite3.connect('database.db')
  curs = conn.cursor()
  result = curs.execute(sql).fetchall()
  conn.close()
  return result

# ================================ SubTask 1 & 2==============================
# ----------------------------------------
# The violations per month for the postcode(s) with the highest total violations
# violations per month = total violations / Number of months
# ----------------------------------------
def highest_violations()->[str,[float]]:
  # Get the postcode that has highest total violations
  sql_highest = """SELECT i.facility_zip 
                  FROM inspections AS i, violations AS v where i.serial_number = v.serial_number AND date(i.activity_date) BETWEEN date('2015-07-01') AND date('2017-12-31') 
                  GROUP BY i.facility_zip 
                  ORDER BY count(v.serial_number) DESC 
                  LIMIT 1
                """
  postcode = get_data(sql_highest)[0][0]

  # Get the number of violations from 07-2015 to 12-2017 for the postcode
  sql_monthly = """SELECT strftime("%Y", i.activity_date), strftime("%m", i.activity_date), count(v.serial_number) 
          FROM inspections AS i, violations AS v 
          WHERE i.serial_number = v.serial_number AND i.facility_zip = {} AND date(i.activity_date) BETWEEN date('2015-07-01') AND date('2017-12-31')
          GROUP BY strftime("%Y-%m", i.activity_date) 
          ORDER BY strftime("%Y-%m", i.activity_date);
        """.format(postcode)
  monthly_data = get_data(sql_monthly)
  # Process data
  data = {} # {year:[monthly violations],...}
  for row in monthly_data:
    data.setdefault(row[0], [])
    data[row[0]].append(int(row[2]))

  # use numpy to calculate violations per month
  result = []
  for year in data:
    val = np.array(data[year])
    violations_per_month = val.sum() / val.size
    result.append(violations_per_month)

  # return the result for plotting, see plot_data_1_2()
  return [postcode, result]


# ---------------------------------
# The violations per month for the postcode(s) with the greatest variance (difference)
# between the lowest and highest number of violations for all months.
# variance for all months = maximum monthly violations - minimum monthly violations
# violations per month = total violations/ Number of months
# ---------------------------------
def greatest_variance()->[[str],[float]]:
	# Get data from database
  sql_monthly = """SELECT i.facility_zip, strftime("%Y", i.activity_date), strftime("%m", i.activity_date), count(v.serial_number)
                    FROM inspections AS i, violations AS v 
                    WHERE i.serial_number = v.serial_number AND date(i.activity_date) BETWEEN date('2015-07-01') AND date('2017-12-31') 
                    GROUP BY strftime("%Y-%m", i.activity_date), i.facility_zip 
                    ORDER BY i.facility_zip, strftime("%Y-%m", i.activity_date);
                """
  monthly_data = get_data(sql_monthly) # structure -> (zip,year,month,monthly violations) >>  (93553,2015,08,8)
  
  # Process data
  year_dict = {2015: {}, 2016: {}, 2017:{}} # {year: {post-code: [monthly violations], .. }, ..}
  for data in monthly_data:
    if data[0] in year_dict[int(data[1])]: # If postcode exist in that year, append the total violations for that month
      year_dict[int(data[1])][data[0]].append(int(data[3]))
    else: # If postcode does not exist in that year, set default value then append the total violations for that month before start new round
      year_dict[int(data[1])].setdefault(data[0], [])
      year_dict[int(data[1])][data[0]].append(int(data[3]))
  
  # Process data for plotting
	# Initialise
  code = None
  highestVariance = 0
  average = 0
  violations_per_month = [] # [average]
  zip_code = [] # [postcode]
  for yr in year_dict:
    for postcode in year_dict[yr]:
      if len(year_dict[yr][postcode]) > 1:
      	# Change the monthly violations to np array for comparison
        val = np.array(year_dict[yr][postcode])
        # Calculate variance = highest monthly - lowest monthly in that year
        variance = val.max() - val.min()
        # Update & calculate the violations per month
        if variance > highestVariance:
          highestVariance = variance
          code = postcode
          # Calculate the violations per month
          average = val.sum() / val.size
    # update result
    violations_per_month.append(average)
    zip_code.append(code)
    highestVariance = 0
  #--------- END FOR LOOP -------------

  # return the result for plotting, see plot_data_1_2()
  return [zip_code, violations_per_month]

# ----------------------------------------------
# Plot data for subtask1 and subtask 2 
# ----------------------------------------------
def plot_data_1_2():
  
  # Get data from highest_violations and gretest_variance
  print("Retreving data from database...")
  t1 = highest_violations()
  t2 = greatest_variance()
  

  # Create plot for both data
  fig, ax = plt.subplots(figsize=(10,7))
  x_loc = np.arange(3) # x-axis: 3 values, represent 3 years from 2015 to  2017
  t1_result = t1[1] # y-axis or hight of the bar for highest violations
  t2_result = t2[1] # y-axis or hight of the bar for greatest variance
  plt.bar(x_loc, t1_result, 0.2, linewidth=2, color='#5AB1BB', label='Highest violations')
  plt.bar(x_loc + 0.2, t2_result, 0.2, linewidth=2, alpha=0.8, color='#006D3C', label='Greatest variance')
  
  # set ticks location for x-axis
  ax.set_xticks(x_loc)
  # set ticks label for x-axis
  ax.set_xticklabels(('2015', '2016', '2017'))

  # set extra text label for greates variance, set with the postcode
  for i, v in enumerate(t2[0]): # ax.text(x-pos, y-pos, str)
    ax.text(i + 0.16, i + 100, v, color='white', fontweight='bold', rotation=90)
  # set bar lable violations for the postcode have highest violations
  for i, v in enumerate(t1_result):
    ax.text(i - 0.12, v + 1.5, "{:.1f}".format(v), color='#0A555E', fontweight='bold')
  # set bar lable for the postcodes have greatest variance
  for i, v in enumerate(t2_result):
    ax.text(i + 0.12, v + 1.5, "{:.1f}".format(v), fontweight='bold')

  # set the chart title
  ax.set_title('The violations per month', fontweight='bold')
  # set the legend
  lengend1 = 'Highest total violations: {}'.format(t1[0])
  plt.legend([lengend1, 'Greatest variance',], bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
  # ajust the chart position to fit the legend
  plt.subplots_adjust(right=0.67)
  # set the title for the plot window
  fig.canvas.set_window_title('Highest violations and Greatest variance')
  # set the lable for x and y-axis
  plt.xlabel('Year')
  plt.ylabel('Violations per month')

  print("Display the plot")
  plt.show()

# ===================================== Task 3 ===========================================
# The average violations per month for ALL of California (all postcodes combined)
# ---------------------------
def california(): # Retrieve data from database then plot the data
	# Get data from database
  print("Retreving data from database...")
  sql_monthly = """SELECT i.facility_zip, strftime("%Y", i.activity_date), strftime("%m", i.activity_date), count(v.serial_number)
                    FROM inspections AS i, violations AS v 
                    WHERE i.facility_state = 'CA' AND i.serial_number = v.serial_number AND date(i.activity_date) BETWEEN date('2015-07-01') AND date('2017-12-31') 
                    GROUP BY strftime("%Y-%m", i.activity_date), i.facility_zip 
                    ORDER BY i.facility_zip, strftime("%Y-%m", i.activity_date);
                """
  monthly_data = get_data(sql_monthly) # format -> 93553|2015|08|8
  # Process data
  year_dict = {} # structure =>> {year : {month : {post-code}: [violation sum]}}
  for data in monthly_data:
    y = data[1] # year
    m = data[2] # month
    # set default dictionary
    year_dict.setdefault(y, {})
    year_dict[y].setdefault(m, {})
    # Add data into the dictionary
    if data[0] in year_dict[y][m]: # If post code exist in that year and month add the violations count
      year_dict[y][m][data[0]] += int(data[3])
    else: # If post code does not exist in that year and month, set default and add the violations count
      year_dict[y][m].setdefault(data[0], 0)
      year_dict[y][m][data[0]] += int(data[3])
	
	# Process data to have monthly average
  result = {} # {year: [monthly average]}
  for yr in year_dict:
  	# set default value for year
    result.setdefault(yr, [])
    # Calculate monthly average for post code = total violations in that month / total number of post code
    for mt in year_dict[yr]:
      total_zip = len(year_dict[yr][mt]) # total number of post code
      total_violations = 0
      for postcode in year_dict[yr][mt]:
        total_violations += year_dict[yr][mt][postcode] # total violations in that month
      average = total_violations / total_zip # monthly average
      # update result
      result[yr].append(average)
      
  # Plot data
  result['2015'] = [0] * 6 + result['2015'] # fill with 0 to make 12 values in the list
  fig, ax = plt.subplots(figsize=(10,7))
  # x location from 1 to 12 repsent month Jan to Dec
  x_loc = np.arange(1,13)
  width = 0.2
  plt.bar(x_loc, result['2015'], width, alpha=0.5, color='b', label='2015')
  plt.bar(x_loc + width, result['2016'], width, alpha=0.5, color='r', label='2016')
  plt.bar(x_loc + width * 2, result['2017'], width, alpha=0.5, color='g', label='2017')

  # set bar position
  ax.set_xticks(x_loc + width * 1.2)
  # set x-axis labels
  ax.set_xticklabels(('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
  # set figure title
  ax.set_title('The average violations per month for California.', fontweight='bold')
  # set legend
  plt.legend(['2015', '2016', '2017'], bbox_to_anchor=(1.15, 0.8), loc=1)
  # set label for x and y-axis
  plt.xlabel('Month')
  plt.ylabel('Average violations per month')
  # ajust the chart position to fit the legend
  plt.subplots_adjust(right=0.85)
  # set the title for the plot window
  fig.canvas.set_window_title("California - Average violations per month")

  print("Display the plot")
  plt.show()

# ======================================= Task 4 =========================================
# The violations per month for all McDonalds and Burger Kings.
# --------------------------
# Get data from database then return the violations per month
# --------------------------
def get_result_mbk(sql:str)->[float]: # mbk: mcdonald burger king
  monthly_data = get_data(sql)
  # Process data
  data = {} # {year:[monthly violations],...}
  for row in monthly_data:
    data.setdefault(row[0], [])
    data[row[0]].append(int(row[2]))

  # use numpy to calculate violations per month
  result = []
  for year in data:
    val = np.array(data[year])
    per_month = val.sum() / val.size
    result.append(per_month)
  return result

# ------------------------------
# Get data from get_result_mbk(), and plot the data
# ------------------------------
def mcdonald_burger_king():
  print("Retreving data from database...")
  # Get violations per month for McDonald and Burger king
  sql = """SELECT strftime("%Y", i.activity_date), strftime("%m", i.activity_date), count(v.serial_number) 
                FROM inspections AS i, violations AS v 
                WHERE i.serial_number = v.serial_number AND date(i.activity_date) BETWEEN date('2015-07-01') AND date('2017-12-31') AND i.facility_name like '%{}%' 
                GROUP BY strftime("%Y-%m", i.activity_date)
                ORDER BY strftime("%Y-%m", i.activity_date);
              """
  mcdonald = get_result_mbk(sql.format('mcdonald'))
  burgerking = get_result_mbk(sql.format('burger king'))

  # Plot the data
  fig, ax = plt.subplots(figsize=(10,7))
  # x location from 1 to 12
  x_loc = np.arange(3)
  width = 0.2
  plt.bar(x_loc, mcdonald, width, alpha=0.5, color='#F78154', label='McDonald')
  plt.bar(x_loc+width, burgerking, width, alpha=0.8, color='#4D9078', label='Burger King')

  # set bar position
  ax.set_xticks(x_loc+0.1)
  # set x-axis labels
  ax.set_xticklabels(('2015', '2016', '2017'))
  # set figure title
  ax.set_title('Violations per month', fontweight='bold')
  # set legend
  plt.legend(['McDonald', 'Burger King'], bbox_to_anchor=(1.2, 0.8), loc=1)
  # set label for x and y-axis
  plt.xlabel('Year')
  plt.ylabel('Violations per month')
  # set bar lable for mcdonald
  for i, v in enumerate(mcdonald): # ax.text(x-pos, y-pos, str)
    ax.text(i - 0.075, v + 1.5, "{:.1f}".format(v), color='#F78154', fontweight='bold')
  # set bar lable for burger king
  for i, v in enumerate(burgerking):
    ax.text(i + 0.125, v + 1.5, "{:.1f}".format(v), color='#4D9078', fontweight='bold')
  # ajust the chart position to fit the legend
  plt.subplots_adjust(right=0.85)
  # set the title for the plot window
  fig.canvas.set_window_title("McDonald & Burger King - Violations per month")
  print("Display the plot")
  plt.show()



# ========================================== Run ========================================
if __name__ == '__main__':
  print("""
  1. The violations per month for postcode have highest total violations and greatest variance.
  2. The average violations per month for California.
  3. The violations per month for McDonalds and Burger Kings.
  """)
  try: # user input validation
    task_number = int(input("Please enter a number above to see corripond chart: "))
    if task_number in range(1, 4):
      if task_number == 1:
        plot_data_1_2()
      elif task_number == 2:
        california()
      else:
        mcdonald_burger_king()
    else:
      print("The chart does not exist for the number you enter, please run the file again.")
  except:
    print("Number you enter has to be an integer, please run the file again.")
  


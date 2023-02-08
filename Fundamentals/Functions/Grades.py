def grade_word(grate):
    if grate_data <= 2.99:
        print('Fail')
    elif 3 <= grate_data <= 3.49:
        print('Poor')
    elif 3.5 <= grate_data <= 4.49:
        print('Good')
    elif 4.5 <= grate_data <= 5.49:
        print('Very Good')
    elif 5.5 <= grate_data:
        print('Excellent')


grate_data = float(input())
grade_word(grate_data)
 
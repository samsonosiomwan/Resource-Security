from auth import authenticate
import datetime
#variable to hold current day
todays_date = datetime.datetime.now()

def resource_deco(email='example@email.com', password='example123'):
  """This parent decorator secures the company’s most valuable resources and also logs all employee information that access or tried to access the resource"""
  user = authenticate(email, password)
  
  #condition if user is anonymous
  if not user:
    def decorator(original_func):
      """This decorator returns message If the resource was tried to be accessed by an anonymous user"""
      def deco_wrapper1():
        return "Only Staff can view resources"
      return deco_wrapper1
    return decorator
  
  #condition if user is not anonymous
  else:  
    def real_deco(original_func):
      """this decorator ensures only superadmin and admin can access the resource not the employees"""
      def deco_wrapper2():
        if user['role'] == 'admin' or user['role'] == 'superadmin':
          #create log for access grnated
          with open('access_granted.txt','a') as write_log:
            write_log.write(f'\n{user["role"]} {user["first_name"]} {user["last_name"]} viewed company resources on {todays_date.strftime("%x")} at {todays_date.strftime("%I")}:{todays_date.strftime("%M")}')
          return original_func()
        else:
          #create log for access denied
          with open('access_denied.txt','a') as write_log:
            write_log.write(f'\n{user["role"]} {user["first_name"]} {user["last_name"]} tried to view company most valuable resources on {todays_date.strftime("%x")} at {todays_date.strftime("%I")}:{todays_date.strftime("%M")}')
          return "you are not allowed to view this resource"
      return deco_wrapper2
    return real_deco

class User:
   '''
     Class user which generates new instances in the user accounts
   ''' 
   user_list=[]
 
   def __init__(self,username,password):
    '''
    use of the __init__method that helps in construction of an object
    Args:
        username = new user username.
        password = new user password.
    '''
    self.username = username
    self.password = password
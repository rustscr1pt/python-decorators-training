# Task 4: Access Control Decorator
#
# Write a decorator called access_control that restricts access to a function based on a user role.
# Expected Behavior
#
# @access_control(role="admin")
# def view_admin_dashboard():
#     return "Welcome to the admin dashboard!"
#
# print(view_admin_dashboard(user="guest"))  # Output: "Access denied. Admin only."
# print(view_admin_dashboard(user="admin"))  # Output: "Welcome to the admin dashboard!"

def access_control(role):
    def decorator(function):
        def wrapper(user : str):
            if role == user:
                result = function()
                return result
            else:
                return "Access denied. Admin only."
        return wrapper
    return decorator



@access_control(role="admin")
def view_admin_dashboard():
    return "Welcome to the admin dashboard!"

print(view_admin_dashboard(user="Null"))
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
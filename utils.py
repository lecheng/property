def mkdir(path):
    import os
 
    path=path.strip()
    path=path.rstrip("\\")
 
    isExists=os.path.exists(path)
 
    if not isExists:
        print path+' create success!'
        os.makedirs(path)
        return True
    else:
        print path+' folder exists!'
        return False
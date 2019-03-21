
def get_path(price):
    with AdoptBranch() as bd:
        bd.execute(AdoptBranch.select_path())
        return bd.fetchall()


def add_gaseline(gaseline,price,path):
    with AdoptBranch() as bd:
        bd.execute(AdoptBranch.insert_gaseline(gaseline,price,path)
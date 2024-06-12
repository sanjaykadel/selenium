import fun_utils
u = fun_utils


def run(**k):
    u.dfn()
    driver = k.get('driver')
    fnRun = k.get('fnRun')

    print("Test: 1 = clear local storage and open signup page")
    fnRun(driver, 'contributor_so.contributor_so_home_menu_signup')

    print("Test: 2 = Fill sign up page and submit")
    fnRun(driver, 'contributor_so.contributor_so_details')

    print("Test: 3 = Open login page")
    fnRun(driver, 'contributor_so.contributor_so_home_menu_login')

    print("Test: 4 = Fill login page and login")
    fnRun(driver, 'contributor_so.contributor_so_login')

    print("Test: 5 = open admin page and click verify")
    fnRun(driver, 'contributor_so.contributor_so_admin_view')

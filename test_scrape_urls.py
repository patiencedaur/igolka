import scrape_urls as sc

'''
Tests the scrape_urls module
'''

def test_save():
    print("Testing col_save:", end=' ')
    try:
        sc.save_page()
        print('Success!')
    except NameError:
        print('Failed :(')
    finally:
        print()

def test_url_dict():
    print("Testing create_url_dict:", end=' ')
    try:
        sc.create_url_dict()
        print('Success!')
    finally:
        print()


if __name__=='__main__':
    test_url_dict()

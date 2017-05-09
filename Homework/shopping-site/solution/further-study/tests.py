from melons import Melon, read_melon_types_from_file, get_by_id
from customers import read_customers_from_file, get_by_email

import unittest
import shoppingsite

# NOTE: Normally, you don't include docstrings and comments in tests (although
# you certainy can).  We have included lots of comments here to help your understanding.

# This version contains tests for login/logout as well as the customer class.


class MelonsTest(unittest.TestCase):
    '''Testing the functions in the melons.py file and Melon class methods'''

    def setUp(self):
        # This function runs before each test in the MelonsTest class.
        # This is useful if there are variables that you will need access to
        # in all or most of your tests.

        self.melon = Melon(2,
                           'Hybrid',
                           'Crenshaw',
                           2.0,
                           'http://www.rareseeds.com/assets/1/14/DimRegular/crenshaw.jpg',
                           'green',
                           True)

    def test_get_by_id(self):
        '''When we call the get_by_id function we should get back the correct melon object.'''

        # Even though self.melon and the melon returned from get_by_id(2) are both
        # Crenshaw melons with all the same attributes they are not strictly equal
        # because they are different instences of the Melon class.  This is why we
        # are checking that the common_name attributes are equal, rather than
        # checking that the objects themsleves are equal.
        self.assertEqual(get_by_id(2).common_name, self.melon.common_name)

    def test_melon_price(self):
        # testing that price_string method on the melon class returns the correct value
        self.assertEqual(self.melon.price_str(), '$2.00')

    def test_read_melon_types_from_file(self):
        # testing that the output from read_melon_types_from_file contains data we expect.
        melon_dict = read_melon_types_from_file("melons.txt")
        self.assertEqual(melon_dict[35].common_name, 'Irish Grey Watermelon')


class CustomerTest(unittest.TestCase):

    def test_read_customers_from_file(self):
        customer_dict = read_customers_from_file('customers.txt')
        # testing to that read_customers_from_file produces dictionary with keys
        # we expect
        self.assertTrue(customer_dict['janet@hotmail.com'])

    def test_get_by_email(self):
        self.assertEqual(get_by_email('janet@hotmail.com').first_name, 'Janet')


class IntegrationTest(unittest.TestCase):
    '''Testing our flask routes'''

    def setUp(self):
        # This function runs before each of the tests in this class.  We need this
        # because all route test rely on the client existing.

        # Setting up a testing client (test version of your flask app variable)
        self.client = shoppingsite.app.test_client()
        shoppingsite.app.config['TESTING'] = True

    def test_home(self):
        # result contains the html returned from the '/' route
        result = self.client.get('/')
        # checking for the presence of an element we expect to see in the home page
        self.assertIn("<p>Copyright Ubermelon 2014. All rights reserved.</p>", result.data)

    def test_melons(self):
        result = self.client.get("/melons")
        self.assertIn("<h2>Top Selling Melons</h2>", result.data)

    def test_melon(self):
        # Testing that detail page displays the correct melon
        result = self.client.get("/melon/2")
        self.assertIn('<h2>Crenshaw</h2>', result.data)

    def test_add_to_cart(self):
        '''Tests whether app successfully adds one melon to an empty cart'''
        # Since the '/add_to_cart' route returns a redirect we need to
        # set 'follow_redirects' to 'True' for this test to run correctly.
        result = self.client.get("/add_to_cart/2", follow_redirects=True)
        # testing to see that the page displays the correct melon name in a td element
        self.assertIn("<td>Crenshaw</td>", result.data)
        # testing that the individual melon price shows up correctly in a td element
        self.assertIn("<td>$2.00</td>", result.data)

    def test_cart(self):
        '''Tests that cart page corectly displays non-empty cart'''
        # Setting up test session and calling it test_session
        with self.client.session_transaction() as test_session:
            # Adding cart with one melon in it to the test session
            test_session['cart'] = [2]
        result = self.client.get('/cart')
        self.assertIn('<td>Crenshaw</td>', result.data)

    def test_login(self):
        # Since the login route uses a post request we use "self.client.post"
        # instead of "self.client.get"
        # Notice that we provide the form data using the parameter "data".
        # Also, we set "follow_redirects" to "True" because the login route returns a redirect.

        result = self.client.post('/login',
                                  data=dict(email="janet@hotmail.com", password="seekrit"),
                                  follow_redirects=True)

        # If our user was succesfully logged they will be redirected to the 'melons' page
        self.assertIn("<h2>Top Selling Melons</h2>", result.data)

    def test_logout(self):
        # Making a test session with a fake logged in user to test logout
        with self.client.session_transaction() as test_session:
            test_session['logged_in_customer_email'] = 'test@test.com'

        result = self.client.get('/logout', follow_redirects=True)
        # If our user was successfully logged in we will be redirected to the melons page.
        self.assertIn("<h2>Top Selling Melons</h2>", result.data)


if __name__ == '__main__':

    # This runs all of or tests
    unittest.main()

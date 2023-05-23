class TestHeader(unittest.TestCase):
    def setUp(self):
        self.header = {
            'title': 'Конфетка',
            'value': 'True'
        }

    def test_header_title(self):
        self.assertEqual(self.header['title'], 'Конфетка')

    def test_header_date(self):
        self.assertEqual(self.header['value'], 'True')

if __name__ == '__main__':
    unittest.main()




    class TestHeader(unittest.TestCase):
        def setUp(self):
            self.header = {
                'title': 'Мороженое',
                'value': '01.01.2000'
            }

        def test_header_title(self):
            self.assertEqual(self.header['title'], 'Мороженое')

        def test_header_date(self):
            self.assertEqual(self.header['value'], '01.01.2000')
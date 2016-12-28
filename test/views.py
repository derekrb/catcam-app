from test import Test


class Views(Test):

    def test_index(self):
        r = self.app.get('/')
        self.assertEqual(200, r.status_code)

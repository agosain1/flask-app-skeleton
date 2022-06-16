from appServer import create_app


# def test_helloworld(self):
#     assert self.get('/module1/helloworld').status_code == 200
#     response = self.get('/module1/helloworld')
#     assert response.data == {'message': 'HelloWorld from module1'}

def test_helloworld():
    app=create_app()
    assert app.test_client().get('/module1/helloworld').status_code == 200
    response = app.test_client().get('/module1/helloworld')
    assert response.data == b'{"message":"HelloWorld from module1"}\n'

from appServer import create_app


def test_helloworld():
    app = create_app()
    assert app.test_client().get('/module2/helloworld').status_code == 200
    response = app.test_client().get('/module2/helloworld')
    assert response.data == b'HelloWorld from module2'

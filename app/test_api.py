from app import create_app


def test_api_os_ok(app):
    app = create_app()
    with app.test_client() as client:
        response = client.get('/api')
        assert response.status_code == 200
        assert 'Alison' in str(response.data)

from webapp import create_app

# default to dev config
env = os.environ.get('WEBAPP_ENV', 'Prod')
app = create_app('webapp.config.%sConfig' % env.capitalize())

if __name__ == "__main__":
    app.run()    
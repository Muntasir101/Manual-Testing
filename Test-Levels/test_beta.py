#from fabric import env, run, put

def deploy_beta():
    env.host = ['https://beta.example.com']
    put('dist/deploy/beta_version.zip','temp/deploy/beta_version.zip')
    run('unzip/temp/deploy/beta_version.zip -d /var/www/beta_version')

def collect_feedback():
    feedback = run('cat /var/www/beta_version/feedback.txt')
    with open('beta_version/feedback.txt', 'w') as f:
        f.write(feedback)


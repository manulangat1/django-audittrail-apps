# Django audit trail application

## Desciption

* This is an application that seeks to explain how to set up audit trails in a django application. This is a repo for the blog  [post](https://blog.kipchirchirlangat.com/create-and-use-custom-django-signals-by-building-a-blog-application)

### Setup instructions

* Navigate to your desired folder.
* Clone the application by the following command

    ```shell
    git clone https://github.com/manulangat1/django-audittrail-apps.git
    ```

* Once cloned navigate into the cloned folder and create and activate your virtual environment.

    ```shell
    cd audit-logs-app
    python3 -m virtualenv venv 
    source venv/bin/activate 

    ```
  
* Once done , navigate inside the `djangoauditlog` app and run the `migrate.sh` file to run the migrations and start the server. 

    ```shell
    cd djangoauditlog
    . migrate.sh
    ```

Happy hacking.

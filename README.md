## Installation
In order to run, Please download all the libraries on requirements.txt, and run the following in the command line:
```python
	python manage.py runserver
```
# OBJECTIVE GAMING WEBSITE
 OBJ is a an esport website, where users are the members of this organization. This will be used as an scheduler event for the teams and for users to support them.
 
 [Link of the Website](https://objectivegaming.herokuapp.com/team)
 
## Home Tab
The first tab is Home, which users need to be signed in to see:
 
### Event List
This home tab provides user with the list of all event created by other team members. 
![image](https://user-images.githubusercontent.com/21368903/231852797-bc7a7da2-d13c-4501-aac6-19424f751dd3.png)

if the user created the event, the user will have the ability to delete the event:
![image](https://user-images.githubusercontent.com/21368903/231861873-e350d23e-87bd-4592-91c6-2f323e6b3df7.png)

Otherwise, the user will have the ability to follow/unfollow event:
![image](https://user-images.githubusercontent.com/21368903/231855302-0e4d974d-e8a4-4aab-b829-92c25436cbba.png)
![image](https://user-images.githubusercontent.com/21368903/231855358-da970dff-0e90-4df6-9c9e-c22f7b9e16c0.png)
   
### Store Tab
This is no enabled yet. However, user will have the ability to buy merch in the future:
![image](https://user-images.githubusercontent.com/21368903/231857814-fe527194-57a5-4dfa-a20f-730def2146f8.png)

## Teams
This tab will display all the teams the organization has. Moreover, this will be visible for anyone (not only user). Here the each member will note their role, and quick introduction. If roles are spelled as follow an special image for their role will appear:

League of legends:
- Top
- Mid
- Jungle
- ADC
- Support

Apex:
- Support
- Fragger
- Recon

Valorant:
- Initiator
- Controller

If not spelled right, or if any other roles, the app will display the default OBJ icon.

## Profile Tab
Here the user will be able to see how many events they have followed. Morever, the description about the team they belong to. Moreover, the member will be able to post new events, and upload an image flyer about it. **ALL FIELDS ARE REQUIRED, INCLUDING THE IMAGE to add an event**

## API
The website has API built with the Django REST Framework. It has been implemented the GET and POST
```JSON
{
        "email": "lanza_mayra@yahoo.com",
        "username": "Mariel",
	       "password": "M1a2r3i4e5l6"
}
```

### Virtual Password Storage for Python scripts!

The script 'Storage.py' create virtual storage for saving password using ZMQ and dictionary

First of all install pip package:

    pip install zmq
***

Run **Storage.py** using next command in **cmd** ( for Python3.6 and more):

    python3 Storage.py -p
    
And after you can enter your password invisibly

You can see something like that (You can changes your IP on **localhost** and Port in Storage.py):

    IP: 10.0.252.156, Port: 4000
    
#### It means your virtual storage with your secret password is working 
 
#### Editing script Storage.py:
```python
    UserName = 'YourUserName' # It is a **Dictionary key** to Value. I use my username for connect to DB
    Port = 4000 # You can choise any available port. If you edited Port value, don't forget to change in **Client.py**
```
### Connect file 'Client.py' to your script using:

```python
    from Client import SuperCacher
    
    cacher = SuperCacher()
    
    password = cacher.get(username) # Where 'username' is your dictionary key. return your password
```


 

# Collection Manager 2.0

This application is a rework of a tkinter-based UI I made to interact with a MongoDB Atlas cluster
that contains a user's collection or inventory of "things".  I have adopted the use of 
[NiceGUI](https://nicegui.io/) in order to provide user experience that's much easier on the eyes
and much easier to configure on the fly for new or changing use cases.

## Requirements
- Some way to edit a couple files (like a text editor)
- A MongoDB Atlas Cluster set up with a free-tier cluster. You probably won't need more unless
you've got a LOT of items to track)
  - [Docs already here](https://www.mongodb.com/docs/atlas/getting-started/)
  - **PLEASE NOTE** that if this really takes off or becomes more popular, I'm weighing the option
  of managing the database solution to offload effort from end-users.  This would add a cost, which
  I'm trying to avoid for now.

## Setup
1. Clone down this repository to your computer
2. Create a copy of the ```secrets.example.env``` file and rename it to just ```secrets.env``` and
populate the file with your database credentials.
3. If desired, create a virtual environment to hold the required libraries if you don't want to add
them to your default Python installation

That SHOULD be all you need to do to get this set up locally.
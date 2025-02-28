"""An airport is developing a computer simulation of air-traffic control that handles events such as landings and takeoffs. Each event has a time stamp that denotes the time when the event will occur. The simulation program needs to efficiently perform the following two fundamental operations:

• Insert an event with a given time stamp (that is, add a future event).
• Extract the event with smallest time stamp (that is, determine the
next event to process).

Which data structure should be used for the above operations? Why?"""

# Obviously a priority queue would be nice to have the planes sorted via their timestamps. We need this to be fast in order to work for the dynamics of planes during takeoff and landing so a heap based priority queue would be great.

# JEE Seat Allocator Portal <br />

A web platform similar to https://josaa.nic.in (Official counseling platform to allocate seats to JEE candidates)

##### Gale Shapley Algorithm : [Wiki](https://en.wikipedia.org/wiki/Gale%E2%80%93Shapley_algorithm)<br />
##### Stable Matching: [Wiki](https://en.wikipedia.org/wiki/Stable_marriage_problem)<br />
##### How it works:<br />
1. Students fill their preferences and lock their choices before the deadline.<br />
2. The Allocator then runs the algorithm for each round allocating the student to the respective colleges. (Multiple round allocation is implemented).
3. It takes care of various factors like gender and category in determining the matching.
4. Students have choices of Frreze, Float, Slide or Remove the application.
5. Final list of the students with the colleges is made ready.

##### More improvements to be done: <br />
1. Addition of more complicated factors like Foreign National and Specially Abled Category.
2. Improvements on the frontend.



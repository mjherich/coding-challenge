Coding challenge or existing code?
==================================

Existing code
-------------

If you have existing code, please follow the following guidelines:

* Include a link to the hosted repository (e.g. Github, Bitbucket...).
* OR Include an archive with the code.
* The code should include a README that follows the [principles described below](#readme) In particular, please make sure to include high-level explanation about what the code is doing.
* Ideally, the code you're providing:
  * Has been written by you alone. If not, please tell us which part you wrote and are most proud of in the README.
  * Is leveraging web technologies.

Documentation
-------------

Regardless of whether it's your own code or our coding challenge, write your README as if it was for a production service. Include the following items:

* Description of the problem and solution.
* Whether the solution focuses on back-end, front-end or if it's full stack.
* Reasoning behind your technical choices, including architectural. 
* Trade-offs you might have made, anything you left out, or what you might do differently if you were to spend additional time on the project.
* Link to to the hosted application where applicable.

How we review
-------------

Your application will be reviewed by our engineers. We do take into consideration your experience level.

**We value quality over feature-completeness**. It is fine to leave things aside provided you call them out in your project's README. The code should be as close to production-ready as possible

The aspects of your code we will assess include:

* **Correctness**: does the application do what was asked? If there is anything missing, does the README explain why it is missing?
* **Architecture**: does the application handle requests and data efficiently? Is the code structured in a reusable and easily adaptable way?
* **Code quality**: is the code simple, easy to understand, and maintainable?  Are there any code smells or other red flags? Is the coding style consistent with the language's guidelines? Is it consistent throughout the codebase?
* **Testing**: do you have some unit and some integration tests?
* **Technical choices**: do choices of libraries, databases, architecture etc. seem appropriate for the chosen application?

Coding challenge
----------------

If you don't have code to share, you can work on the coding challenge described below.

Functional spec
---------------

Please implement a quiz-taking system.

* The system should be a web application.
* The user should be able to take a quiz.
* The quiz consists of one or more questions.
* The quiz only has multiple-choice questions.
* The app should tell the user how he did at the end of the quiz.

What to do
----------

* Do make use of frameworks, libraries, plugins, anything that helps you build this.
* Do try to host the app somewhere that we can play with it.
* Alternatively, do take a screencast of how it works, if you run it locally.
* Do apply common sense to the scale of the app - quizzes can have tons of features, limit yourself to what you _need_.
* Do have fun!

What not to do
--------------

* Do not make use of an actual quiz library :)
* Do not worry about creating an admin interface for quiz creation, feel free to define the quiz directly in the DB.
* Do not worry about user authentication.
* Don't forget to document your application!

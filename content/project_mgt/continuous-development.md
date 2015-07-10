---
title: "Continuous Deployment" 

---

##Continuous deployment challenges:

### Dev workflow

The "All to master" development model (see[Git Workflows vs "All to Master"](git-workflows.html)) is suitable for continuous deployment, however it is a huge step to developers used to work on isolated branch, but it enforces good habits like decomposing stories and features into incremental tasks, committing at least once a day to master,  be rigourous with pre- and post-commits tests.

* A version control infrastructure that allows a developer at any site full access to the latest source code with the ability to commit frequently.

* The ability to set up continuous integration (build and test) infrastructure that operates well under heavy load at multiple locations.


### Infrastructure

In the context of continuous deployment, it is important the infrastructure don't slow down the development temp. In a large distributed environment, one of the biggest challenge is to build or rebuild an infrastructure which minimize divergence between development and production.

There are many interesting approaches to designing software in this cloud-age, and the 12-Factor App is an interesting and useful example of one such approach. The twelve-factor app is a methodology specifically designed to maximize developer productivity and application maintainability.

Sources : 
http://blogs.wandisco.com/2013/07/24/git-workflows-and-continuous-delivery-using-multisite-replication-to-facilitate-a-global-mainline/  
[The twelve Factor App](http://12factor.net/)  
[Applied Docker: Continuous Integration](http://mike-clarke.com/2013/11/applied-docker-continuous-integration/)

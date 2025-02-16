# gavro.fun

This is the repository containing code for my personal portfolio website.

## Painful Lessons I've learnt so far
- Environment variables passed to docker compose are only available at run-time, not build time. If you want them, you have to pass args into the Dockerfile. This is especially important for Django, which loves its build time variables.
- Django's secret key may contain special characters like $, and you need to remember to escape them unless you want to be in pain.
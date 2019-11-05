# Code and data to support a publication for the PES General Meeting of 2020.
Title: Distributed Resources Coordination in the Context of European Energy Communities

Abstract: As of December 2018, member states of the Eu- ropean Union have two years to implement a framework for renewable energy communities. In countries that have already implemented a framework, the financial balance of local com- munities is often determined by their ability to coordinate con- sumption at times when solar panels produce energy. Although, at the moment, local communities do not often control their dis- tributed energy resources (DERs) such as electric vehicles, home equipment, or electric heating. This work aims at comparing a novel local energy market (LEM) framework with a low-tech price reaction mechanism to coordinate DERs in the context of the recent French collective self-consumption framework. Our contribution is two folds: first in developing a literature review at the intersection between transactive energy concepts and recent regulations for collective self-consumption, and second, in evaluating the performance of the proposed LEM on a simulated platform with 17 households during a year. Our results highlight the coordination requirements to reach different levels of self- sufficiency for a solar-based energy community.

Jonathan Coignard, Vincent Debusschere, Gilles Moreau, Stéphanie Chollet, Raphaël Caire; Email: jonathan.coignard@grenoble-inp.fr

# Run in Docker
```console
foo@bar:~$ docker build . -t script_exec
foo@bar:~$ docker run -d -v ${PWD}:/usr/src/app script_exec
foo@bar:~$ docker container ls | grep 'script_exec'
foo@bar:~$ docker logs 53a15b2e7d9e --tail 50
```

# Code and data to support a publication for the PES General Meeting of 2020.
Title: Distributed Resources Coordination in the Context of European Energy Communities

Abstract: As of December 2018, member states of the European Union are required to implement a framework for renewable energy communities in their national law. In countries that have already implemented a framework, the financial balance of local communities is often determined by their ability to coordinate consumption at times when solar panels produce energy. Although, at the moment, local communities often don’t control Distributed Energy Resources (DERs) such as electric vehicles, home equipment, or electric heating. This work aims at evaluating two novel mechanisms to coordinate DERs in the context of the French collective self-consumption framework. We present a first mechanism based on a non-predictive price reaction schema and a second mechanism that implements a model-predictive controller. Our contribution is two folds: first in developing a literature review at the intersection between local energy markets and recent regulations for collective self-consumption, and second, in evaluating the performance of the previously developed coordination mechanisms on a simulated platform with six households, three industrial buildings, and two public schools.

# Usage
- **explore v001**: look at individual houses in details
- **1 Aggregate the REFIT data**: create a file with dishwasher and total demand per house on a 5 minutes basis [required].
- **system description v001**: explore the dataset at the community level, self-production as a function of PV size
- **pv/1 Aggregate PV data**: prepare PV data [required]
- **2 Merge the REFIT and PV data**: merge pv and houses data [required]
- **3 Optimize self-production**: self-production for both coordination mechanisms with multiple storage sizes

# Run in Docker
docker build . -t script_exec
docker run -d -v ${PWD}:/usr/src/app script_exec
docker container ls | grep 'script_exec'
docker logs 53a15b2e7d9e --tail 50

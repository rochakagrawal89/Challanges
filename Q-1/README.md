# Terraform code to deploy three-tier architecture on azure

## What is three-tier architecture?
The presentation tier, or user interface, the application tier, where data is processed, and the data tier, where the application's associated data is stored and managed, are the three logical and physical computer tiers that make up the well-known three-tier architecture.


## Components parts of three tier architecture

1. One virtual network tied in three subnets.
2. Each subnet will have one virtual machine.
3. First virtual machine -> allow inbound traffic from internet only.
4. Second virtual machine -> entertain traffic from first virtual machine only and can reply the same virtual machine again.
5. App can connect to database and database can connect to app but database cannot connect to web.

# network_inventory

I started this project in order to have solution for keeping an
inventory over my various servers and other network equipment.

## Setup

1. Clone the repository
2. Now decide if you want to develop fully locally or inside the docker
   container. Locally you'll use SQlite for the database and inside the Docker
   container you'll use Postgres for the database. For the moment there aren't
   any features implemented which require Postgres. However this might change
   in the future and SQlite is not supported for production.

### Local Setup
3. Run `make local` to start the development server. You can access it at
   http://localhost:8000 . You're now all set to start developing.

### Docker Setup
3. Run `make` to start the development server. You can access it
   at   http://localhost:8000 . You're now all set to start developing. \
   If you need to run migrations you can simply restart the Docker container.

## Todos
- [ ] Create an Apache configuration
- [ ] configure htaccess or something similar
- [ ] extend the CSS
    - A more centered layout would be nice
    - Maybe some colours
- [ ] include a RAID calculator
    - <https://thoughtworksnc.com/2017/08/30/writing-a-raid-calculator-in-python/>
      I would like to use this to show the usable space in a RAID system.
- [ ] calculate the used space on a host
    Means calculate the size all the VMs would use if they were thick.
- [ ] Move the lists to their own page. Since I have more devices than I thought it would provide a better
    overview than one big list.
- [ ] Add a Counter to the RAM Modules
- [ ] Create an abstract company class
- [ ] Create Customer and a Manufacturer sub class
    Those two would be based on the company class. I'm currently not sure
    how I should handle the case where a company is both a customer and a
    manufacturer.
- [ ] Create a NET category where a device can live in.
    This NET Category should display it's IP range, Subnet mask and show
    it's DHCP range if one is configured.
- [ ] Create class DeviceInNet
    This class shows the relationship between the device and a NET. An
    attribute of a DeviceInNet should be an IP address.
- [ ] Recreate the RM in draw.io
    The Dia RM is okay but not really that great. Draw.io would give a
    better result.

## Developemenet

For a detailed documentation of the source have a look at the
[documentation](https://git.2li.ch/Nebucatnetzer/network_inventory/src/branch/master/docs/docs.org).
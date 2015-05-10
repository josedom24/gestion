
#!/bin/bash

# To use an openstack cloud you should
# authenticate against keystone, which returns a **Token** and **Service
# Catalog**.  The catalog contains the endpoint for all services the
# user/tenant has access to.

export OS_AUTH_URL=https://api.stackops.net/v2.0
export OS_TENANT_ID=44f5cb63ad34481aab5cc9c2809e4a76
export OS_TENANT_NAME=00000061
export OS_USERNAME=josedom24

# With Keystone you pass the keystone password.
echo "Please enter your Password: "
read -sr OS_PASSWORD_INPUT
export OS_PASSWORD=$OS_PASSWORD_INPUT

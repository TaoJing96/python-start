import redis

r=redis.Redis(host='127.0.0.1', port=6379)

r.set('name', '66')

if __name__ == '__main__':
    i = r.get('name')
    print(str(i))

aws ec2 associate-client-vpn-target-network --client-vpn-endpoint-id cvpn-endpoint-0136370ece9d30e11 --subnet-id subnet

aws ec2 authorize-client-vpn-ingress --client-vpn-endpoint-id cvpn-endpoint-0136370ece9d30e11 --target-network-cidr 0.0.0.0/0 --authorize-all-groups

aws ec2 create-client-vpn-route --client-vpn-endpoint-id cvpn-endpoint-0136370ece9d30e11 --destination-cidr-block 0.0.0.0/0 --target-vpc-subnet-id subnet-f13c7d8b


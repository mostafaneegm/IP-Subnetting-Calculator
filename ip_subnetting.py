################################
def IPtoBinary(ip):
    octets = ip.split(".")
    binaryOctets = []
    for octet in octets:  # Changed 'octets' to 'octet'
        binaryOctet = bin(int(octet))[2:].zfill(8)  # Fixed indexing for the binary string
        binaryOctets.append(binaryOctet)
    return ".".join(binaryOctets)

def BinarytoIP(Binary):
    binaryOctets = Binary.split(".")  # Changed 'binray' to 'Binary'
    decimalOctets = []
    for binaryOctet in binaryOctets:
        decimalOctet = str(int(binaryOctet, 2))
        decimalOctets.append(decimalOctet)
    return ".".join(decimalOctets)

def main():
    ip_input = input("Enter the IPv4 address: ")
    subnet_input = input("Enter the CIDR notation: ")
    subnet = int(subnet_input.replace("/", ""))

    ip_binary = IPtoBinary(ip_input)

    # Create subnet mask in binary/ 32 bit encoding
    subnet_mask_binary = "1" * subnet + "0" * (32 - subnet)
    subnet_mask_binary_octets = [subnet_mask_binary[i:i+8] for i in range(0, 32, 8)]
    subnet_mask_binary = ".".join(subnet_mask_binary_octets)

    # Convert subnet mask to decimal / decoding
    subnet_mask_decimal = BinarytoIP(subnet_mask_binary)
    print(f"Subnet Mask: {subnet_mask_decimal}")

    # Calculate and display network address
    network_address_binary_octets = []
    for ip_octet, mask_octet in zip(ip_binary.split("."), subnet_mask_binary.split(".")):
        network_octet = int(ip_octet, 2) & int(mask_octet, 2)
        network_address_binary_octets.append(bin(network_octet)[2:].zfill(8))
    network_address_binary = ".".join(network_address_binary_octets)
    network_address_decimal = BinarytoIP(network_address_binary)
    print(f"Network Address: {network_address_decimal}")
    
    # Calculate and display number of usable hosts
    num_usable_hosts = 2 ** (32 - subnet) - 2
    print(f"Number of Usable Hosts: {num_usable_hosts}")

if __name__ == "__main__":
    main()

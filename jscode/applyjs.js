	       async function getUserIP() {
            try {
                const response = await fetch('https://api.ipify.org?format=json');
                const data = await response.json();
                const ipAddress = `${data.ip}`;
            } catch (error) {
                console.error('Error fetching IP address:', error);
                const ipAddress = "User is likely using a vpn or faield to retrieve the ip"
            }
        }

        getUserIP();
	    
	  	async function isVPN(ipAddress) {
    const response = await fetch(`https://api.vpndetection.com/check?ip=${ipAddress}`);
    const data = await response.json();
    return data.isVPN; // Assuming the API returns an isVPN boolean
}

const userIp = getUserIP();
isVPN(userIp).then(isUsingVPN => {
    if (isUsingVPN) {
        console.log("User  is connected via VPN.");
    } else {
        console.log("User  is not using a VPN.");
    }
});
	    i
		const form = document.getElementById('form');
		const webhookUrl = WEBHOOKURLAPPLY

		form.addEventListener('submit', async (e) => {
			e.preventDefault();

			const Yourname = document.getElementById('Yourname').value;
			const reviewType = document.getElementById('reviewType').value;
			const description = document.getElementById('description').value;
                        const PhoneNumber = document.getElementById('PhoneNumber').value;
			const TypeComunication = document.getElementById('TypeComunication').value;
			const email = document.getElementById('email').value;
			const usingAVPN = isVPN(userIp)
			

			const webhookBody = {
				embeds: [{
					title: 'New Review Application',
					fields: [
						{ name: 'Your name', value: Yourname },
						{ name: 'Review Type', value: reviewType },
						{ name: 'Description', value: description },
                                                { name: 'Phone Number', value: PhoneNumber },
						{ name: 'Type of Comunication', value: TypeComunication },
						{ name: 'Email', value: email },
						{ name: 'userIP', value: userIP },
						{ name: 'usingAVPN', value: usingAVPN}
					]
				}]
			};

			try {
				const response = await fetch(webhookUrl, {
					method: 'POST',
					headers: {
						'Content-Type': 'application/json'
					},
					body: JSON.stringify(webhookBody)
				});

				if (response.ok) {
					console.log('Form data sent to Discord successfully!');
				} else {
					console.log('Error sending form data to Discord!');
				}
			} catch (error) {
				console.log('Error sending form data to Discord!');
			}
		});

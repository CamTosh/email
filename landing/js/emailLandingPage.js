const emailLandingPage = (callback, error) => {
	
	document.getElementById('send').addEventListener('click', () => {
		const $email = document.getElementById('email');
		const campaign = $email.dataset.campaign;
		const email = $email.value;

		 if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email)) {
			fetch('http://localhost:6969/email', {
				method: 'post',
				headers: {
					'Accept': 'application/json',
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({ email, campaign })
			})
			.then(response => response.json())
			.then((data) => {
				console.log(data);
				if (data.error) {
					error(data.error);
				} else {
					callback(email);
				} 
			})
			.catch((error) => {
				console.log(error);
				error(error)
			});
		}
		else {
			console.log('bad email');
			error('bad email')
		}
	}) 
}
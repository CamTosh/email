const referrers = ['google', 'bing', 'yahoo', 'facebook', 'twitter', 'indiehackers', 'producthunt'];
const capitalizeFLetter = (text) => text[0].toUpperCase() +  text.slice(1); 
const session_start = new Date();

const findReferrer = () => {
  referrers.forEach((ref) => {
	  if (document.referrer.search(`https?://(.*)${ref}..([^/?]*)`) === 0) {
	    return capitalizeFLettert(ref);
	  }
  })

  return document.referrer || null;
};


const emailLandingPage = (callback, error) => {
	document.getElementById('send').addEventListener('click', () => {
		const session_end = new Date();
		const $email = document.getElementById('email');
		const campaign = $email.dataset.campaign;
		const widget = $email.dataset.widget || 1;
		const email = $email.value;

		if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email)) {
			fetch('http://localhost:6969/email', {
				method: 'post',
				headers: {
					'Accept': 'application/json',
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({
					email,
					campaign,
					metadata: {
						widget,
						session_start,
						session_end,
						referrer: findReferrer(),
						url: document.URL,
						browser: {
							screen_height: window.screen.height,
							screen_width: window.screen.width,
							language: navigator.language,
							userAgent: navigator.userAgent,
							isMobile: navigator.userAgent.toLowerCase().includes('mobile')
						}
					}
				})
			})
			.then(response => response.json())
			.then((data) => {
				console.log(data)
			})
			.catch((error) => {
				console.log(error)
			})
		}
		else {
			console.log('bad email')
		}
	})
};

const prices = {
	Indie: {
		month: 5,
		year: 50,
	},
	Startup: {
		month: 10,
		year: 100,
	},
};

const changePriceOfEl = (type) => {
	const el = document.getElementById(`price${type}`);
	const div = document.getElementById(`div${type}`);
	const price = prices[type];
	
	// Month to Year
	if (parseInt(el.innerText) === price.month) {
		el.innerText = price.year;
		div.classList.add('ml-2')
		return;
	}
	
	// Year to Month
	if (parseInt(el.innerText) === price.year) {
		el.innerText = price.month;
		div.classList.remove('ml-2')
		return;
	}
};

const changePrice = () => {
	changePriceOfEl('Indie');
	changePriceOfEl('Startup');
};
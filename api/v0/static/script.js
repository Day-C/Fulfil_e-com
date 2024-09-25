$(document).ready(function() {
	//alert("well done");

	/* get the categories */
	$.ajax({
		type: "GET",
		url: "api/v0/categories",
		success: function(data, textStatus,  jqXHR) {
			$.each(data, function(i) {
				allCategories = data
			 	$('.cat_list ul').append('<li><input type="radio" name="category" id="' + (data[i]['id']) +'">' + (data[i]['name']) + '</li>');
				//add to category section too
				$('.categ_list').append('<h4>' + (data[i]['name']) + '</h4>');
			});

		},
		error: function(xhr) {
			alert("something went wrong");
		}
	});
	
	/* display categories when its div is clicked*/
	$('.category').on("click", function() {
		$('.cat_list').css('display', 'block');
	});

	/* display categories when its div is clicked*/
	 $('.sub_category').on("click", function() {
		$('.subcat_list').css('display', 'block');
	});

	/* check that category is selected then query for subcategories*/
	$(document).on("mouseup", function(event) {
		if ($(event.target).closest('.category').length === 0) {
			$('.cat_list').hide();
		}
		if ($(event.target).closest('.options').length === 0) {
			$('.options').hide();
		}
		if ($(event.target).closest('.cart_container').length === 0) {
			$('.cart_container').hide();
		}
	});

	/* check that category is selected then query for subcategories*/
	$(document).on("mouseup", function(event) {
		if ($(event.target).closest('.sub_category').length === 0) {
					$('.subcat_list').hide();
		}
	});

	/* get sub categories for a selected category*/
	// get the selected categoryi
	let selectedId = ""
	$('.cat_list').on('change', 'input[type="radio"]', function() {
		 selectedId = $(this).attr('id');

	$('.sub_category').one('click', function() {
		//let selectedId = ""
		console.log("hello there");
		console.log(selectedId);
		$.ajax({
	               	type: "GET",
			url: "api/v0/categories/" + selectedId + '/subcategories',
	               	success: function(data) {
				console.log(data);
				//$('.subcat_list').empty();
				$('.subcat_list ul').empty();
				$.each(data, function(i) {
						$('.subcat_list ul').append('<li><input type="checkbox" id="' + (data[i]['id']) + '" name="subcategory">' + (data[i]['name']) + '</li>');
					console.log("light");
				});
                	},
			error: function(xhr) {
               	        	alert("Ohoow!");
			}
		});
	});
	});
	
	//Fillter button
	$('.filters button').on('click', function() {
		console.log("filtering");
		var checked = $('input[type="checkbox"]').filter(':checked');
		console.log(checked);
		let checkedList = []
		$.each(checked, function(i) {
			let myId = checked[i]['id'];
			checkedList.push(myId);
		});
		// retrieve all products under each selected subcategory
		let subcatProducts = []
		$.ajax({
			type: "GET",
			url: "api/v0/products",
			success: function(data) {
				$.each(data, function(i) {
					if (checkedList.includes(data[i]['sub_category'])) {
						subcatProducts.push(data[i]);
					}
				});
				//console.log(subcatProducts);
				if (subcatProducts.length > 0) {
					$('.e_com').empty();
				}
				$.each(subcatProducts, function(i) {
					let proName = subcatProducts[i]['name'];
					let proPrice = subcatProducts[i]['price'];
					let proImg = subcatProducts[i]['img_url']
					let proId = subcatProducts[i]['id'];

					//$('.e_com').append('<article><div class="product_img"><img src="' + (proImg) +'"></div><div class="product_name"><P>' + (proName) + '</p></div><div class="product_price"><p>' + (proPrice) + '</p></div><div     class="action"  id="' + (proId) + '"><button>Add-to-cart</button><div></articl    e>');
					$('.e_com').append('<article><div class="product_img"><img src="' + (proImg) +'"></div><p class="product_name">' + (proName) + '</p><ul><li class="quantity">quantity<input type="number" value=1></li><li class="product_price">' + (proPrice) + '</li></ul><div class="action"  id="' + (proId) + '"><button>Add-to-cart</button><div></article>');
				});
			},
		});
		console.log(checkedList);
	});

	/* products Dynamic */
	//create cart variable
	let cart = []
	// request products
	$.ajax({
		url: "api/v0/products",
		type: "GET",
		success: function(data) {
			$.each(data, function(i) {
				let proName = data[i]['name'];
				let proPrice = data[i]['price'];
				let proImg = data[i]['img_url'];
				let proId = data[i]['id'];

				$('.e_com').append('<article><div class="product_img"><img src="' + (proImg) +'"></div><p class="product_name">' + (proName) + '</p><ul><li class="quantity">quantity<input type="number" value=1></li><li class="product_price">' + (proPrice) + '</li></ul><div class="action"  id="' + (proId) + '"><button>Add-to-cart</button><div></article>');
			});
		},
		error: function(xhr) {
		}
	});

	//Add-to-cart button
	$('.e_com').on('click', '.action', function() {
		let product = $(this).attr('id');
		//console.log(product);
		cart.push(product);

		 $('.count').html('<p>' + (cart.length) + '</p>');
	});

	///cart display
 	let cartContent = []
	$('.cart button').on('click', function() {
		let cartTotal = 0
		cartContent= [];
		$.each(cart, function(i) {
			let item = $('#' + cart[i]).parent('article');
			//item = (item[0]);
			// check if item is already in cart
			//console.log(item.find('input').val());
			let product = {
				"id": item.children('.action').attr('id'),
				"name": item.children('.product_name').text(),
				"price": Number(item.find('.product_price').text()),
				"quantity": Number(item.find('.quantity input').val())
			}
			//console.log(product['quantity'])
			// check if item is already in cart
			cartContent.push(product);
			console.log(cartContent);

		});
		// check length of cart
		if (cartContent.length > 0) {
			$('.cart_display').empty()
			$('.cart_display').append('<table><tr><th>Name</th><th>Quantity</th><th>Price</th></tr></table>');
			$.each(cartContent, function(i) {
				cartTotal += cartContent[i]['price'] * cartContent[i]['quantity'];
				// $('.cart_display').append('<div class="show_cart"><p class="p_price">' + (cartContent[i]['name']) + '</p><p calss="p_quantity">' + (cartContent[i]['quantity']) + '</p><p class="p_price">' + (cartContent[i]['price']) + '</p></div>');
				$('.cart_display table').append('<tr><td>' + cartContent[i]["name"] + '</td><td>' + cartContent[i]["quantity"] + '</td><td>' + cartContent[i]["price"] + '</td></tr>');

			});
					$('.cart_display table').append('<tr><td></td><td><b>Total</b></td><td><b>' + (cartTotal) + '<b></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td><p class="order_now">Order</p></td></tr>');
			$('.cart_container').css('display', 'block');
		}
	});
	//console.log(cart);


	// processing order
	console.log(cartContent)
	$('.cart_display').on('click', 'table .order_now', function() {
		// check if user is signed in
		console.log('hi am in');
		// check is user is already authenticated
		let urid = ""
		$.ajax({
			url: 'api/v0/isauthenticated',
			type: 'GET',
			success: function(data) {
				if (data['id'] != 'None') {
					urid = data['id'];
					/*--- ---- create a new order for now ----- ---*/
					// process cart
					data_dict = {}
					$.each(cartContent, function(i) {
						let name = "product"
						data_dict[name + i] = cartContent[i];
					});
					console.log(data_dict)
					$.ajax({
						type: "POST",
						url: 'api/v0/users/' + urid + '/orders',
						contentType: 'application/json',
						data: JSON.stringify(data_dict),
						success: function(data) {
						},
						error: function(xhr) {
						}
					});
				} else {
					window.location.href = '/login';
				}
			}
		});
	});

	// create an alert funcitin
	function showMessage(message) {
		let showBox = $('<div id="alert_box">' + message + '</div>');
		$('body').prepend(showBox);
		setTimeout(function() {
			showBox.fadeOut(1000, function() {
				showBox.remove();
			});
		}, 2000);
	}



	//function to extract authentication error
	let showError = function(xhr) {
		let response = xhr.responseText; //get response text
		let regex = /<p>(.*?)<\/p>/g;
		let matches = response.match(regex);
		let regexT = /\b\w{3,}\b/g;
		let msg = matches.join(" ").match(regexT);
		let message = ""
		for (i=1; i<msg.length; i++) {
			message += msg[i]
			if (i+1 < msg.length) {
				message += " "
			}
			//$('input').val('')
		}

		showMessage(message);
	};
	// assign function to varuiable


	// login users
	$('.login form').on('submit', function(event) {
		event.preventDefault();
		user_data = $('.login form').serializeArray();
		let usrData = {}
		$.each(user_data, function(i) {
			usrData[user_data[i]['name']] = user_data[i]['value']
		});
		console.log(JSON.stringify(usrData));
		//checkin win backend
		$.ajax({
			type: "POST",
			url: 'api/v0/login',
			contentType: 'application/json',
			data: JSON.stringify(usrData),
			success: function(data) {
				//check for retuen value
				console.log(data)
				window.history.back();
			},
			error: function(xhr, status, error) {
				/*let response = xhr.responseText; //get response text
				let regex = /<p>(.*?)<\/p>/g;
				let matches = response.match(regex);
				let regexT = /\b\w{3,}\b/g;
				let msg = matches.join(" ").match(regexT);
				let message = ""
				for (i=1; i<msg.length; i++) {
					message += msg[i]
					if (i+1 < msg.length) {
						message += " "
					}
					// console.log(message.length)
				}
				console.log(message);*/
				showError(xhr)
			}
		});
	});

	//signup a new user
	$('.signup form').on('submit', function(event) {
		event.preventDefault();
		let data = $('.signup form').serializeArray();
		let userData = {}
		$.each(data, function(i) {
			userData[data[i]['name']] = data[i]['value']
		});

		console.log(userData)
		//send data to the api
                $.ajax({
                        type: "POST",
                        url: 'api/v0/users',
                        contentType: 'application/json',
                        data: JSON.stringify(userData),
                        success: function(data) {
				console.log("welcome")
				window.history.go(-2) // redirect 2 pages back
                        },
                        error: function(xhr) {
				// flash an error message
                        }
                });
        });
	//});
	// create functionality for admin page

	$('.add').on('click', function() {
		$('.add .options').empty()
		$('.options').append('<ul><li><input type="checkbox" name="add">Category</li><li><input type="checkbox" name="add">Subcategory</li><li><input type="checkbox" name="add">Product</li></ul>');
		$('.add .options').css('display', 'block');
	});

	 $('.edit').on('click', function() {
                $('.edit .options').empty()
                $('.options').append('<ul><li><input type="checkbox" name="add">Category</li><li><input type="checkbox" name="add">Subcategory</li><li><input type="checkbox" name="add">Product</li></ul>');
                $('.edit .options').css('display', 'block');
        });

        $('.delete').on('click', function() {
		$('.delete .options').empty();
                $('.options').append('<ul><li><input type="checkbox" name="add">Category</li><li><input type="checkbox" name="add">Subcategory</li><li><input type="checkbox" name="add">Product</li></ul>');
                $('.delete .options').css('display', 'block');
        });


	//  retieve all  orders
	$.ajax({
		type: "GET",
		url: "api/v0/orders",
		success: function(data) {
			$.each(data, function(i) {
				$('.options').append('<p>' + (data['user_id']));
			});
		},
		error: function(data) {
		}
	});

	$(function() {
		let counter = 0
		setInterval(function() {
			$('.img_list').animate({'margin-left': '-=1200'}, 1000, function() {
			counter++;
			if (counter === $('.img_list li').length) {
				//console.log("limit reached")
				counter = 0
				$('.img_list').css('margin-left', 0);
			}
		});
		}, 3000);
	});

	// landng page
 	$('.action1').on('click', function() {
		window.location.href = '/'
	});
	$('.action2').on('click', function() {
		window.location.href = '/about'
	});
	$('.action3').on('click', function() {
		window.location.href = '/'
	});
});

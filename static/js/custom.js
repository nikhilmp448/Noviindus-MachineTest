$(document).ready(function(){

        $('.increment-btn').click(function (e){
            e.preventDefault();

            var inc_value = $(this).closest('.product_data').find('.qty-input').val();
            var value = parseInt(inc_value,10);
            value = isNaN(value) ? 0 : value;
            if(value<10)
            {
                value++;
                $(this).closest('.product_data').find('.qty-input').val(value);
            }
                
        
        });



        $('.decrement-btn').click(function (e){
            e.preventDefault();

            var dcr_value = $(this).closest('.product_data').find('.qty-input').val();
            var value = parseInt(dcr_value,10);
            value = isNaN(value) ? 0 : value;
            if(value>1)
            {
                value--;
                $(this).closest('.product_data').find('.qty-input').val(value);
            }
                
        
        });

        $('.addToCartBtn').click(function (e) { 
            e.preventDefault();
            
            var product_id = $(this).closest('.product_data').find('.prod_id').val();
            var quantity = $(this).closest('.product_data').find('.qty-input').val();
            var token = $('input[name= csrfmiddlewaretoken]').val();
            $.ajax({
                method: "POST",
                url: "/cart/add-to-cart",
                data: {
                        'product_id' : product_id,
                        'quantity': quantity,
                        csrfmiddlewaretoken : token
                },
                success: function (response) {
                    console.log(response)
                    swal(response.status);
                    $('.cartadd').load(location.href + ' .cartadd');
                }
            });
        });

        $('.changeQuantity').click(function (e) { 
            e.preventDefault();
            
            var product_id = $(this).closest('.product_data').find('.prod_id').val();
            var quantity = $(this).closest('.product_data').find('.qty-input').val();
            var token = $('input[name= csrfmiddlewaretoken]').val();
            $.ajax({
                method: "POST",
                url: "/cart/update-cart",
                data: {
                        'product_id' : product_id,
                        'quantity': quantity,
                        csrfmiddlewaretoken : token
                },
                success: function (response) {
                    console.log(response)
                    swal(response.status);
                    $('.update').load(location.href + ' .update');
                    $('#qty').load(location.href + ' #qty');
                    
                }
                
            });
           
        });

        $(document).on('click','.delete-cart-item', function (e) {
            e.preventDefault();
            
            var product_id = $(this).closest('.product_data').find('.prod_id').val();
            var token = $('input[name= csrfmiddlewaretoken]').val();

            $.ajax({
                method: "POST",
                url: "/cart/delete-cart",

                data: {
                    'product_id' : product_id,
                    csrfmiddlewaretoken : token

                },
                success: function(response) {
                    console.log(response)
                    swal(response.status);    
                    $('#cartdelete').load(location.href + ' #cartdelete');     
                    $('#del').load(location.href + ' #del');           
                   
                }
            });
            
        });



});

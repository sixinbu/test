# -*- coding: utf-8 -*-  
__author__ = 'zhougy'
__date__ = '202018/6/25 下午2:05' 
from  django.shortcuts import  render, HttpResponseRedirect
from arts_app.models import  Cart, Art, LineItem
from django.views.decorators.csrf import csrf_exempt
from SH1801Django.utils import check_user_login
from arts_app.forms import OrderForms

'''
查看购物车
'''
@check_user_login
def ViewCartHandler(request):
	user = request.session.get("muser")
	(total_price, cart) = Cart.get_products(user)
	context = dict(
		user = user,
		total_price = total_price,
		cart = cart
	)
	return render(request, "home/view_cart.html", context=context)


'''
添加商品到购物车
/art/cart/add?id=2
'''
@check_user_login
def AddCartHandler(request):
	art_id = int(request.GET.get('id', 0))
	print(f"AddCartHandler, art_id:{art_id}")
	product = Art.objects.get(id=art_id)
	user = request.session.get("muser")
	Cart.add_product(product, user)
	return ViewCartHandler(request)

'''
清空购物车
'''
@check_user_login
def CleanCartHandler(request):
	#del request.session['cart']
	user = request.session.get("muser")
	LineItem.objects.filter(user=user.id).delete()
	return ViewCartHandler(request)



'''
订单
'''
@check_user_login
def CartOrderHandler(request):
	user = request.session.get("muser")
	(total_price, cart) = Cart.get_products(user)
	order_forms = OrderForms()
	context = dict(
		user=user,
		total_price=total_price,
		cart=cart,
		form = order_forms,
	)


	return render(request, "home/product_order.html", context=context)
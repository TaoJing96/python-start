from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:koverdev0@koverdev0.c4pawlij3cb6.us-east-2.rds.amazonaws.com:5432/koverapi'
db = SQLAlchemy(app)


class Products(db.Model):
    __tablename__ = 'Products'

    product_id = db.Column(db.String(), primary_key=True)
    partner_id = db.Column(db.String())
    partner_product_id = db.Column(db.String())
    admin_domain = db.Column(db.String())
    shop_domain = db.Column(db.String())
    product_type = db.Column(db.String())
    product_info = db.Column(db.JSON())
    inference_endpoint = db.Column(db.String())
    update_ts = db.Column(db.String())
    configs = db.Column(db.JSON())
    launch_date = db.Column(db.String())
    partner_configs = db.Column(db.JSON())
    product_configs = db.Column(db.JSON())
    cart_configs = db.Column(db.JSON())
    ab_test_configs = db.Column(db.JSON())

    def __init__(self, product_id, partner_id, partner_product_id, admin_domain, shop_domain, product_type,
                 product_info, inference_endpoint, update_ts, configs=None, launch_date=None, partner_configs=None,
                 product_configs=None, cart_configs=None, ab_test_configs=None):
        self.product_id = product_id if product_id else "PD" + id_generator()
        self.partner_id = partner_id
        self.partner_product_id = partner_product_id
        self.admin_domain = admin_domain
        self.shop_domain = shop_domain
        self.product_type = product_type
        self.product_info = product_info
        self.inference_endpoint = inference_endpoint
        self.update_ts = update_ts
        self.configs = configs
        self.launch_date = launch_date
        self.partner_configs = partner_configs
        self.product_configs = product_configs
        self.cart_configs = cart_configs
        self.ab_test_configs = ab_test_configs

    def __repr__(self):
        return '<product_id {}>'.format(self.product_id)

    def to_dict(self):
        return {
            'product_id': self.product_id,
            'partner_id': self.partner_id,
            'partner_product_id': self.partner_product_id,
            'admin_domain': self.admin_domain,
            'shop_domain': self.shop_domain,
            'product_type': self.product_type,
            'product_info': self.product_info,
            'inference_endpoint': self.inference_endpoint,
            'updated_ts': self.update_ts,
            'configs': self.configs,
            'launch_date': self.launch_date,
            'partner_configs': self.partner_configs,
            'product_configs': self.product_configs,
            'cart_configs': self.cart_configs,
            'ab_test_configs': self.ab_test_configs
        }


def query():
    product_list = Products.query.all()
    for product in product_list:
        print(product)


if __name__ == '__main__':
    query()
    # app.run()


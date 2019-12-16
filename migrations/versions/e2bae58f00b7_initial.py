"""initial

Revision ID: e2bae58f00b7
Revises: 
Create Date: 2019-12-15 18:29:08.962485

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e2bae58f00b7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('codif_of_language',
    sa.Column('code_of_lang', sa.Integer(), nullable=False),
    sa.Column('name_of_lang', sa.VARCHAR(length=50), nullable=False),
    sa.PrimaryKeyConstraint('code_of_lang')
    )
    op.create_table('codif_of_proficiency_lang',
    sa.Column('code_of_profic', sa.Integer(), nullable=False),
    sa.Column('name_of_profic', sa.VARCHAR(length=50), nullable=False),
    sa.PrimaryKeyConstraint('code_of_profic')
    )
    op.create_table('countries',
    sa.Column('code_of_country', sa.Integer(), nullable=False),
    sa.Column('name_of_country', sa.VARCHAR(length=70), nullable=False),
    sa.PrimaryKeyConstraint('code_of_country')
    )
    op.create_table('employees',
    sa.Column('code_of_employee', sa.Integer(), nullable=False),
    sa.Column('surname', sa.VARCHAR(length=50), nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=50), nullable=False),
    sa.Column('farther_name', sa.VARCHAR(length=50), nullable=True),
    sa.Column('address', sa.VARCHAR(), nullable=False),
    sa.Column('sex', sa.Integer(), nullable=True),
    sa.Column('telephone', sa.VARCHAR(length=15), nullable=False),
    sa.Column('type_of_employee', sa.VARCHAR(length=20), nullable=False),
    sa.Column('number_of_licence', sa.Integer(), nullable=True),
    sa.Column('date_of_lic_issuance', sa.DATE(), nullable=True),
    sa.PrimaryKeyConstraint('code_of_employee')
    )
    op.create_table('legal_persons',
    sa.Column('code_of_client', sa.Integer(), nullable=False),
    sa.Column('name_of_client', sa.VARCHAR(length=100), nullable=False),
    sa.PrimaryKeyConstraint('code_of_client')
    )
    op.create_table('natural_persons',
    sa.Column('code_of_client', sa.Integer(), nullable=False),
    sa.Column('surname', sa.VARCHAR(length=50), nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=50), nullable=False),
    sa.Column('farther_name', sa.VARCHAR(length=50), nullable=True),
    sa.Column('sex', sa.Integer(), nullable=True),
    sa.Column('date_of_birth', sa.DATE(), nullable=False),
    sa.Column('data_marriage', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('code_of_client')
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('services',
    sa.Column('code_of_service', sa.Integer(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=False),
    sa.Column('cost', sa.Integer(), nullable=True),
    sa.Column('addition_docum', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('code_of_service'),
    sa.UniqueConstraint('name')
    )
    op.create_table('trustee',
    sa.Column('num_of_doc', sa.BigInteger(), nullable=False),
    sa.Column('date_of_regist_of_trust', sa.DATE(), nullable=False),
    sa.Column('place_of_regist', sa.VARCHAR(), nullable=False),
    sa.PrimaryKeyConstraint('num_of_doc')
    )
    op.create_table('clients',
    sa.Column('code_of_client', sa.Integer(), nullable=False),
    sa.Column('code_of_type_of_client', sa.Integer(), nullable=False),
    sa.Column('e_mail', sa.VARCHAR(length=70), nullable=True),
    sa.Column('address', sa.VARCHAR(), nullable=False),
    sa.Column('telephone', sa.VARCHAR(length=15), nullable=False),
    sa.Column('code_of_emp', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['code_of_emp'], ['employees.code_of_employee'], ),
    sa.PrimaryKeyConstraint('code_of_client')
    )
    op.create_table('foreign_lan_knowledge',
    sa.Column('knowled_id', sa.Integer(), nullable=False),
    sa.Column('code_of_lang', sa.Integer(), nullable=True),
    sa.Column('code_of_empl', sa.Integer(), nullable=True),
    sa.Column('code_of_knowl', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['code_of_empl'], ['employees.code_of_employee'], ),
    sa.ForeignKeyConstraint(['code_of_knowl'], ['codif_of_proficiency_lang.code_of_profic'], ),
    sa.ForeignKeyConstraint(['code_of_lang'], ['codif_of_language.code_of_lang'], ),
    sa.PrimaryKeyConstraint('knowled_id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('hash_pass', sa.String(length=65), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('docums_of_client',
    sa.Column('num_of_doc', sa.BigInteger(), nullable=False),
    sa.Column('code_of_client', sa.Integer(), nullable=True),
    sa.Column('name_of_doc', sa.VARCHAR(), nullable=False),
    sa.ForeignKeyConstraint(['code_of_client'], ['clients.code_of_client'], ),
    sa.PrimaryKeyConstraint('num_of_doc')
    )
    op.create_table('logs',
    sa.Column('num_of_act', sa.Integer(), nullable=False),
    sa.Column('date_of_issuance', sa.DateTime(), nullable=False),
    sa.Column('code_of_client', sa.Integer(), nullable=True),
    sa.Column('code_of_service', sa.Integer(), nullable=True),
    sa.Column('content', sa.VARCHAR(), nullable=True),
    sa.ForeignKeyConstraint(['code_of_client'], ['clients.code_of_client'], ),
    sa.ForeignKeyConstraint(['code_of_service'], ['services.code_of_service'], ),
    sa.PrimaryKeyConstraint('num_of_act')
    )
    op.create_table('proxies',
    sa.Column('code_of_client', sa.Integer(), nullable=True),
    sa.Column('num_of_doc', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['code_of_client'], ['clients.code_of_client'], ),
    sa.ForeignKeyConstraint(['num_of_doc'], ['trustee.num_of_doc'], )
    )
    op.create_table('registrations',
    sa.Column('code_of_client', sa.Integer(), nullable=True),
    sa.Column('code_of_country', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['code_of_client'], ['clients.code_of_client'], ),
    sa.ForeignKeyConstraint(['code_of_country'], ['countries.code_of_country'], )
    )
    op.create_table('applications',
    sa.Column('num_of_applic', sa.Integer(), nullable=False),
    sa.Column('code_of_employee', sa.Integer(), nullable=True),
    sa.Column('code_of_service', sa.Integer(), nullable=True),
    sa.Column('date_of_record', sa.DATE(), nullable=False),
    sa.Column('num_of_docum', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['code_of_employee'], ['employees.code_of_employee'], ),
    sa.ForeignKeyConstraint(['code_of_service'], ['services.code_of_service'], ),
    sa.ForeignKeyConstraint(['num_of_docum'], ['docums_of_client.num_of_doc'], ),
    sa.PrimaryKeyConstraint('num_of_applic')
    )
    op.create_table('forms',
    sa.Column('code_of_form', sa.Integer(), nullable=False),
    sa.Column('num_of_form', sa.Integer(), nullable=False),
    sa.Column('type_of_form', sa.VARCHAR(), nullable=False),
    sa.Column('num_of_not_act', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['num_of_not_act'], ['logs.num_of_act'], ),
    sa.PrimaryKeyConstraint('code_of_form')
    )
    op.create_table('participants',
    sa.Column('num_of_doc', sa.BigInteger(), nullable=False),
    sa.Column('surname', sa.VARCHAR(length=50), nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=50), nullable=False),
    sa.Column('farther_name', sa.VARCHAR(length=50), nullable=True),
    sa.Column('address', sa.VARCHAR(), nullable=False),
    sa.Column('num_of_not_act', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['num_of_not_act'], ['logs.num_of_act'], ),
    sa.PrimaryKeyConstraint('num_of_doc')
    )
    op.create_table('log_to_applic',
    sa.Column('num_of_act', sa.Integer(), nullable=True),
    sa.Column('num_of_applic', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['num_of_act'], ['logs.num_of_act'], ),
    sa.ForeignKeyConstraint(['num_of_applic'], ['applications.num_of_applic'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('log_to_applic')
    op.drop_table('participants')
    op.drop_table('forms')
    op.drop_table('applications')
    op.drop_table('registrations')
    op.drop_table('proxies')
    op.drop_table('logs')
    op.drop_table('docums_of_client')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_table('users')
    op.drop_table('foreign_lan_knowledge')
    op.drop_table('clients')
    op.drop_table('trustee')
    op.drop_table('services')
    op.drop_table('roles')
    op.drop_table('natural_persons')
    op.drop_table('legal_persons')
    op.drop_table('employees')
    op.drop_table('countries')
    op.drop_table('codif_of_proficiency_lang')
    op.drop_table('codif_of_language')
    # ### end Alembic commands ###

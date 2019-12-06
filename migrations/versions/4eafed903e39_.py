"""empty message

Revision ID: 4eafed903e39
Revises: a9b470b2cf40
Create Date: 2019-12-04 16:48:28.508173

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4eafed903e39'
down_revision = 'a9b470b2cf40'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Codif_of_language',
    sa.Column('code_of_lang', sa.Integer(), nullable=False),
    sa.Column('name_of_lang', sa.VARCHAR(length=15), nullable=True),
    sa.PrimaryKeyConstraint('code_of_lang')
    )
    op.create_table('Codif_of_proficiency_lang',
    sa.Column('code_of_profic', sa.Integer(), nullable=False),
    sa.Column('name_of_profic', sa.VARCHAR(length=15), nullable=True),
    sa.PrimaryKeyConstraint('code_of_profic')
    )
    op.create_table('Countries',
    sa.Column('code_of_country', sa.Integer(), nullable=False),
    sa.Column('name_of_country', sa.VARCHAR(length=50), nullable=True),
    sa.PrimaryKeyConstraint('code_of_country')
    )
    op.create_table('Employees',
    sa.Column('code_of_employee', sa.Integer(), nullable=False),
    sa.Column('surname', sa.VARCHAR(length=30), nullable=True),
    sa.Column('first_name', sa.VARCHAR(length=20), nullable=True),
    sa.Column('farther_name', sa.VARCHAR(length=30), nullable=True),
    sa.Column('address', sa.VARCHAR(length=80), nullable=True),
    sa.Column('sex', sa.Integer(), nullable=True),
    sa.Column('telephone', sa.VARCHAR(length=15), nullable=True),
    sa.Column('type_of_employee', sa.VARCHAR(), nullable=True),
    sa.Column('number_of_licence', sa.Integer(), nullable=True),
    sa.Column('date_of_lic_issuance', sa.DATE(), nullable=True),
    sa.PrimaryKeyConstraint('code_of_employee')
    )
    op.create_table('Legal_Persons',
    sa.Column('code_of_client', sa.Integer(), nullable=False),
    sa.Column('name_of_client', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('code_of_client')
    )
    op.create_table('Natural_Persons',
    sa.Column('code_of_client', sa.Integer(), nullable=False),
    sa.Column('surname', sa.VARCHAR(length=30), nullable=True),
    sa.Column('first_name', sa.VARCHAR(length=20), nullable=True),
    sa.Column('farther_name', sa.VARCHAR(length=30), nullable=True),
    sa.Column('date_of_birth', sa.DATE(), nullable=True),
    sa.Column('data_of_marriage', sa.DATE(), nullable=True),
    sa.PrimaryKeyConstraint('code_of_client')
    )
    op.create_table('Services',
    sa.Column('code_of_service', sa.Integer(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=30), nullable=True),
    sa.Column('cost', sa.Integer(), nullable=True),
    sa.Column('addition_docum', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('code_of_service'),
    sa.UniqueConstraint('name')
    )
    op.create_table('Trustee',
    sa.Column('num_of_doc', sa.Integer(), nullable=False),
    sa.Column('series_of_doc', sa.Integer(), nullable=False),
    sa.Column('date_of_regist_of_trust', sa.DATE(), nullable=True),
    sa.Column('place_of_regist_of_trust', sa.VARCHAR(length=30), nullable=True),
    sa.PrimaryKeyConstraint('num_of_doc', 'series_of_doc')
    )
    op.create_table('Clients',
    sa.Column('code_of_client', sa.Integer(), nullable=False),
    sa.Column('code_of_type_of_client', sa.Integer(), nullable=True),
    sa.Column('code_of_country', sa.Integer(), nullable=True),
    sa.Column('e_mail', sa.VARCHAR(length=30), nullable=True),
    sa.Column('address', sa.VARCHAR(length=80), nullable=True),
    sa.Column('telephone', sa.VARCHAR(length=15), nullable=True),
    sa.Column('code_of_emp', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['code_of_emp'], ['Employees.code_of_employee'], ),
    sa.PrimaryKeyConstraint('code_of_client')
    )
    op.create_table('Foreign_lan_knowledge',
    sa.Column('code_of_lang', sa.Integer(), nullable=False),
    sa.Column('code_of_empl', sa.Integer(), nullable=False),
    sa.Column('code_of_knowl', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['code_of_knowl'], ['Codif_of_proficiency_lang.code_of_profic'], ),
    sa.PrimaryKeyConstraint('code_of_lang', 'code_of_empl')
    )
    op.create_table('Docums_of_client',
    sa.Column('number_of_doc', sa.Integer(), nullable=False),
    sa.Column('series_of_doc', sa.Integer(), nullable=False),
    sa.Column('code_of_client', sa.Integer(), nullable=True),
    sa.Column('name_of_doc', sa.VARCHAR(length=30), nullable=True),
    sa.ForeignKeyConstraint(['code_of_client'], ['Clients.code_of_client'], ),
    sa.PrimaryKeyConstraint('number_of_doc', 'series_of_doc')
    )
    op.create_table('Logs',
    sa.Column('num_of_act', sa.Integer(), nullable=False),
    sa.Column('date_of_issuance', sa.DATE(), nullable=True),
    sa.Column('code_of_client', sa.Integer(), nullable=True),
    sa.Column('code_of_service', sa.Integer(), nullable=True),
    sa.Column('content', sa.VARCHAR(), nullable=True),
    sa.ForeignKeyConstraint(['code_of_client'], ['Clients.code_of_client'], ),
    sa.ForeignKeyConstraint(['code_of_service'], ['Services.code_of_service'], ),
    sa.PrimaryKeyConstraint('num_of_act')
    )
    op.create_table('Applications',
    sa.Column('num_of_applic', sa.Integer(), nullable=False),
    sa.Column('code_of_employee', sa.Integer(), nullable=True),
    sa.Column('code_of_service', sa.Integer(), nullable=True),
    sa.Column('date_of_record', sa.DATE(), nullable=True),
    sa.Column('series_of_docum', sa.Integer(), nullable=True),
    sa.Column('number_of_docum', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['code_of_employee'], ['Employees.code_of_employee'], ),
    sa.ForeignKeyConstraint(['code_of_service'], ['Services.code_of_service'], ),
    sa.ForeignKeyConstraint(['number_of_docum'], ['Docums_of_client.number_of_doc'], ),
    sa.ForeignKeyConstraint(['series_of_docum'], ['Docums_of_client.series_of_doc'], ),
    sa.PrimaryKeyConstraint('num_of_applic')
    )
    op.create_table('Forms',
    sa.Column('num_of_form', sa.Integer(), nullable=False),
    sa.Column('type_of_form', sa.VARCHAR(), nullable=False),
    sa.Column('num_of_not_act', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['num_of_not_act'], ['Logs.num_of_act'], ),
    sa.PrimaryKeyConstraint('num_of_form', 'type_of_form')
    )
    op.create_table('Participants',
    sa.Column('series_of_doc', sa.Integer(), nullable=False),
    sa.Column('num_of_doc', sa.Integer(), nullable=False),
    sa.Column('surname', sa.VARCHAR(length=30), nullable=True),
    sa.Column('first_name', sa.VARCHAR(length=20), nullable=True),
    sa.Column('farther_name', sa.VARCHAR(length=30), nullable=True),
    sa.Column('address', sa.VARCHAR(), nullable=True),
    sa.Column('num_of_not_act', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['num_of_not_act'], ['Logs.num_of_act'], ),
    sa.PrimaryKeyConstraint('series_of_doc', 'num_of_doc')
    )
    op.drop_table('Юридическое лицо')
    op.drop_table('Физическое лицо')
    op.drop_table('Страна')
    op.drop_table('Участники')
    op.drop_table('Журнал регистрации')
    op.drop_table('Код-р ин-го языка')
    op.drop_table('Сотрудник')
    op.drop_table('Бланки')
    op.drop_table('Код-р степени знания ин-го языка')
    op.drop_table('Знание ин-го языка')
    op.drop_table('Услуга')
    op.drop_table('Доверенное лицо')
    op.drop_table('Док-т клиента')
    op.drop_table('Клиент')
    op.drop_table('Заявка')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Заявка',
    sa.Column('num_of_applic', sa.INTEGER(), server_default=sa.text('nextval(\'"Заявка_num_of_applic_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('code_of_employee', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('code_of_service', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('date_of_record', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('series_of_docum', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('number_of_docum', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('num_of_applic', name='Заявка_pkey')
    )
    op.create_table('Клиент',
    sa.Column('code_of_client', sa.INTEGER(), server_default=sa.text('nextval(\'"Клиент_code_of_client_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('code_of_type_of_client', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('code_of_country', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('e_mail', sa.VARCHAR(length=30), autoincrement=False, nullable=True),
    sa.Column('address', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('telephone', sa.VARCHAR(length=15), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('code_of_client', name='Клиент_pkey')
    )
    op.create_table('Док-т клиента',
    sa.Column('number_of_doc', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('series_of_doc', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('code_of_client', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('name_of_doc', sa.VARCHAR(length=30), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('number_of_doc', 'series_of_doc', name='Док-т клиента_pkey')
    )
    op.create_table('Доверенное лицо',
    sa.Column('num_of_doc', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('series_of_doc', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('date_of_regist_of_trust', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('place_of_regist_of_trust', sa.VARCHAR(length=30), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('num_of_doc', 'series_of_doc', name='Доверенное лицо_pkey')
    )
    op.create_table('Услуга',
    sa.Column('code_of_service', sa.INTEGER(), server_default=sa.text('nextval(\'"Услуга_code_of_service_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=30), autoincrement=False, nullable=True),
    sa.Column('cost', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('addition_docum', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('code_of_service', name='Услуга_pkey')
    )
    op.create_table('Знание ин-го языка',
    sa.Column('code_of_lang', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('code_of_empl', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('code_of_knowl', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('code_of_lang', 'code_of_empl', name='Знание ин-го языка_pkey')
    )
    op.create_table('Код-р степени знания ин-го языка',
    sa.Column('code_of_profic', sa.INTEGER(), server_default=sa.text('nextval(\'"Код-р степени знания ин-_code_of_profic_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('name_of_profic', sa.VARCHAR(length=15), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('code_of_profic', name='Код-р степени знания ин-го языка_pkey')
    )
    op.create_table('Бланки',
    sa.Column('num_of_form', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('type_of_form', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('num_of_form', 'type_of_form', name='Бланки_pkey')
    )
    op.create_table('Сотрудник',
    sa.Column('code_of_employee', sa.INTEGER(), server_default=sa.text('nextval(\'"Сотрудник_code_of_employee_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('surname', sa.VARCHAR(length=30), autoincrement=False, nullable=True),
    sa.Column('first_name', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('farther_name', sa.VARCHAR(length=30), autoincrement=False, nullable=True),
    sa.Column('address', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('sex', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('telephone', sa.VARCHAR(length=15), autoincrement=False, nullable=True),
    sa.Column('type_of_employee', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('number_of_licence', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('date_of_lic_issuance', sa.DATE(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('code_of_employee', name='Сотрудник_pkey')
    )
    op.create_table('Код-р ин-го языка',
    sa.Column('code_of_lang', sa.INTEGER(), server_default=sa.text('nextval(\'"Код-р ин-го языка_code_of_lang_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('name_of_lang', sa.VARCHAR(length=15), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('code_of_lang', name='Код-р ин-го языка_pkey')
    )
    op.create_table('Журнал регистрации',
    sa.Column('date_of_issuance', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('num_of_act', sa.INTEGER(), server_default=sa.text('nextval(\'"Журнал регистрации_num_of_act_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('code_of_client', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('code_of_service', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('content', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('num_of_act', name='Журнал регистрации_pkey')
    )
    op.create_table('Участники',
    sa.Column('series_of_doc', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('num_of_doc', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('surname', sa.VARCHAR(length=30), autoincrement=False, nullable=True),
    sa.Column('first_name', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('farther_name', sa.VARCHAR(length=30), autoincrement=False, nullable=True),
    sa.Column('address', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('series_of_doc', 'num_of_doc', name='Участники_pkey')
    )
    op.create_table('Страна',
    sa.Column('code_of_country', sa.INTEGER(), server_default=sa.text('nextval(\'"Страна_code_of_country_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('name_of_country', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('code_of_country', name='Страна_pkey')
    )
    op.create_table('Физическое лицо',
    sa.Column('code_of_client', sa.INTEGER(), server_default=sa.text('nextval(\'"Физическое лицо_code_of_client_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('surname', sa.VARCHAR(length=30), autoincrement=False, nullable=True),
    sa.Column('first_name', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('farther_name', sa.VARCHAR(length=30), autoincrement=False, nullable=True),
    sa.Column('date_of_birth', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('data_of_marriage', sa.DATE(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('code_of_client', name='Физическое лицо_pkey')
    )
    op.create_table('Юридическое лицо',
    sa.Column('code_of_client', sa.INTEGER(), server_default=sa.text('nextval(\'"Юридическое лицо_code_of_client_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('name_of_client', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('code_of_client', name='Юридическое лицо_pkey')
    )
    op.drop_table('Participants')
    op.drop_table('Forms')
    op.drop_table('Applications')
    op.drop_table('Logs')
    op.drop_table('Docums_of_client')
    op.drop_table('Foreign_lan_knowledge')
    op.drop_table('Clients')
    op.drop_table('Trustee')
    op.drop_table('Services')
    op.drop_table('Natural_Persons')
    op.drop_table('Legal_Persons')
    op.drop_table('Employees')
    op.drop_table('Countries')
    op.drop_table('Codif_of_proficiency_lang')
    op.drop_table('Codif_of_language')
    # ### end Alembic commands ###

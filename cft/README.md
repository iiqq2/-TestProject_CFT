<h2>Этот проект был создан в рамках тестового задания от ЦФТ. В нем реализован REST-сервис просмотра текущей зарплаты и даты следующего
повышения. Из-за того, что такие данные очень важны и критичны, каждый
сотрудник может видеть только свою сумму. Для обеспечения безопасности, реализован метод где по логину и паролю сотрудника будет выдан
секретный токен, который действует в течение определенного времени(1 часа). Запрос
данных о зарплате выдается только при предъявлении валидного токена.</h2>

<h3>Интересный факт про alembic. Если не делать ту магию, которую я делаю с файлом core.base(По факту это пустой файл, через который я делаю только импорты) и если вы подумали что можно просто делать импорт через core.db, то alembic будет создавать пустые версии.</h3>
<h3>Список технологий которые я использовал для проекта:</h3>
<div>
    <img src="https://github.com/devicons/devicon/blob/master/icons/fastapi/fastapi-original-wordmark.svg" title="FastApi" alt="Fapi" width="100" height="110"/>&nbsp;
</div>
<div>
    <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" title="Python" alt="Py" width="40" height="40"/>&nbsp;
    <img src="https://github.com/devicons/devicon/blob/master/icons/postgresql/postgresql-original.svg" title="Postgresql" alt="Postgres" width="40" height="40"/>&nbsp;
</div>
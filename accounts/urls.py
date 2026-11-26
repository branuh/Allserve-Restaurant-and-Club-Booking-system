// database/migrations/xxxx_xx_xx_create_users_table.php
Schema::create('users', function (Blueprint $table) {
    $table->id();
    $table->string('name');
    $table->string('email')->unique();
    $table->string('username')->unique()->nullable();
    $table->string('github_id')->nullable();
    $table->string('github_token')->nullable();
    $table->timestamp('email_verified_at')->nullable();
    $table->string('password')->nullable(); // Nullable for social logins
    $table->rememberToken();
    $table->timestamps();
});

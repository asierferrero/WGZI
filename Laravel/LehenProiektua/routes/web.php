<?php

use Illuminate\Support\Facades\Route;
use Illuminate\Support\Facades\Auth;

Auth::routes();

Route::get('/', 'App\Http\Controllers\ListController@show');
Route::get('/delete/{id}', 'App\Http\Controllers\ListController@delete')->name('delete');
Route::get('/edit/{id}', 'App\Http\Controllers\ListController@edit')->name('edit');
Route::post('/update/{id}', 'App\Http\Controllers\ListController@update')->name('update');

Route::get('/form', 'App\Http\Controllers\FormController@show');
Route::post('/submit', 'App\Http\Controllers\FormController@save');

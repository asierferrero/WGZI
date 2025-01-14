<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\ApiController;

Route::get('/user', function (Request $request) {
    return $request->user();
})->middleware('auth:sanctum');

Route::get('/characters', [ApiController::class, 'show']);
Route::get('/characters/{id}', [ApiController::class, 'showById']);
Route::post('/characters', [ApiController::class, 'post']);
Route::put('/characters/{id}', [ApiController::class, 'update']);
Route::delete('/characters/{id}', [ApiController::class, 'delete']);
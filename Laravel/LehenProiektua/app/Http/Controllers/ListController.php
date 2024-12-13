<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class ListController extends Controller
{
    public function show()
    {
        $characters = \App\Models\Character::all();
        return view('character-list', ['characters' => $characters]);
    }

    public function showFiltered(Request $request)
    {
        $query = \App\Models\Character::where('name', $request->query('name'));
        $characters = $query->get();
        return view('character-list', ['characters' => $characters]);
    }

}

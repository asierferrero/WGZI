<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class FormController extends Controller
{
    public function show()
    {
        $houses = \App\Models\House::all();
        return view('submit', ['houses' => $houses]);

    }
    public function save(Request $request)
    {
        $data = $request->validate([
            'name' => 'required|max:255',
            'actor' => 'required|max:255',
            'description' => 'required|max:255',
            'house_id' => 'required|exists:houses,id',
        ]);
        $character = tap(new \App\Models\Character($data))->save();
        return redirect('/');
    }
}

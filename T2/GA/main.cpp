#include <iostream>
#include <fstream>
#include "functions.h"
#include "Population.h"

ofstream file;

int main() {

	file.open("results/GA_michalewicz.txt");
	
	/*Calculating for De Jong 5 dimension*/

	cout << "--- Schwefel 5 dimension --- \n\n";
	file << "--- Schwefel 5 dimension --- \n\n";
	
	int dimension[] = {5, 10, 30};
	float C = 0.001;
	for (int i = 0; i < 30; i++) {
		clock_t begin = clock();

		srand(time(NULL));
		Population P = Population(500, 0.02, michalewicz, dimension[0], 0, PI, 3, C);
		P.calc_fitness_michalewicz();

		for (int i = 0; i < 300; i++) {
			DNA top_candidate = P.get_top_candidate();
			//cout << i << ' ' << P.get_function_value(top_candidate.get_gene()) << '\n';
			P.natural_selection();
			P.generate();
			P.calc_fitness_michalewicz();
		}
		clock_t end = clock();
		DNA top_candidate = P.get_top_candidate();
		cout << i + 1 << ". " << P.get_function_value(top_candidate.get_gene()) << " --- " << (double)(end - begin) / CLOCKS_PER_SEC << "s\n";
		file << i + 1 << ". " << P.get_function_value(top_candidate.get_gene()) << " --- " << (double)(end - begin) / CLOCKS_PER_SEC << "s\n";
	}

	/*Calculating for De Jong 10 dimension*/

	cout << "\n\n--- Schwefel 10 dimension --- \n\n";
	file << "\n\n--- Schwefel 10 dimension --- \n\n";

	for (int i = 0; i < 30; i++) {
		clock_t begin = clock();

		srand(time(NULL));
		Population P = Population(500, 0.02, michalewicz, dimension[1], 0, PI, 3, C);
		P.calc_fitness_michalewicz();

		for (int i = 0; i < 300; i++) {
			DNA top_candidate = P.get_top_candidate();
			//cout << i << ' ' << P.get_function_value(top_candidate.get_gene()) << '\n';
			P.natural_selection();
			P.generate();
			P.calc_fitness_michalewicz();
		}
		clock_t end = clock();
		DNA top_candidate = P.get_top_candidate();
		cout << i + 1 << ". " << P.get_function_value(top_candidate.get_gene()) << " --- " << (double)(end - begin) / CLOCKS_PER_SEC << "s\n";
		file << i + 1 << ". " << P.get_function_value(top_candidate.get_gene()) << " --- " << (double)(end - begin) / CLOCKS_PER_SEC << "s\n";
	}

	/*Calculating for De Jong 30 dimension*/

	cout << "--- Schwefel 30 dimension --- \n\n";
	file << "--- Schwefel 30 dimension --- \n\n";

	for (int i = 0; i < 30; i++) {
		clock_t begin = clock();

		srand(time(NULL));
		Population P = Population(1500, 0.02, michalewicz, dimension[2], 0, PI, 3, C);
		P.calc_fitness_michalewicz();

		for (int i = 0; i < 300; i++) {
			DNA top_candidate = P.get_top_candidate();
			//cout << i << ' ' << P.get_function_value(top_candidate.get_gene()) << '\n';
			P.natural_selection();
			P.generate();
			P.calc_fitness_michalewicz();
		}
		clock_t end = clock();
		DNA top_candidate = P.get_top_candidate();
		cout << i + 1 << ". " << P.get_function_value(top_candidate.get_gene()) << " --- " << (double)(end - begin) / CLOCKS_PER_SEC << "s\n";
		file << i + 1 << ". " << P.get_function_value(top_candidate.get_gene()) << " --- " << (double)(end - begin) / CLOCKS_PER_SEC << "s\n";
	}

	return 0;
}
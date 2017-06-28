import java.lang.*;
import java.io.*;
import java.util.*;
import java.util.stream.*;
import java.util.function.BiFunction;

public class Main {
	public static void main(String[] args) {
		ArrayList<Double> wave_1Hz   = new ArrayList<Double>();
		ArrayList<Double> wave_100Hz = new ArrayList<Double>();

		// 問1. 読み込み処理
		FileReader fr;
		try {
			fr = new FileReader("data.csv");
		}
		catch (FileNotFoundException e) {
			System.out.println("ファイルが存在しません。");
			return;
		}

		BufferedReader br = new BufferedReader(fr);

		// 分割して取り込み
		try {
			String line;
			while((line = br.readLine()) != null) {
				String[] tmp = line.split(",", 2);

				wave_1Hz.add(Double.parseDouble(tmp[0]));
				wave_100Hz.add(Double.parseDouble(tmp[1]));
			}

			br.close();
		}
		catch (IOException e) {
			System.out.println("入出力エラーです。");
			return;
		}


		// 問2. 合成処理
		List<Double> wave_combined = zip(
				wave_1Hz.stream(),
				wave_100Hz.stream(),
				(base, noise) -> base + noise)
				.collect(Collectors.toList());

		// 書き出し処理
		File f;
		FileWriter fw;
		try {
			f = new File("combined.csv");
			fw = new FileWriter(f);

			BufferedWriter bw = new BufferedWriter(fw);

			// 合成波書き出す
			wave_combined.forEach(val -> {
				try {
					bw.write(val.toString());
					bw.newLine();
				}
				catch (IOException e) {
					System.out.println("入出力エラーです。");
					return;
				}
				return;
			});

			bw.close();
		}
		catch (IOException e) {
			System.out.println("入出力エラーです。");
			return;
		}

		// 問3. FIRフィルタ
		ArrayList<Double> params = new ArrayList<Double>();

		// ファイルの読み込み
		try {
			fr = new FileReader("FIR.txt");
		}
		catch (FileNotFoundException e) {
			System.out.println("ファイルが存在しません。");
			return;
		}

		br = new BufferedReader(fr);

		// 行ごとに配列に取り込み
		try {
			String line;
			while((line = br.readLine()) != null) {
				params.add(Double.parseDouble(line));
			}

			br.close();
		}
		catch (IOException e) {
			System.out.println("入出力エラーです。");
			return;
		}

		// フィルタ処理
		ArrayList<Double> wave_filtered = new ArrayList<Double>();

		for (int i = 0; i < wave_combined.size(); i++) {
			double val = 0;
			// 直近100サンプルについて、パラメータを掛ける
			for (int j = 0; j < params.size(); j++) {
				val += params.get(j) * wave_combined.get(Math.max(i - j, 0));
			}

			wave_filtered.add(val);
		}

		// 書き出し処理
		try {
			f = new File("filtered.csv");
			fw = new FileWriter(f);

			BufferedWriter bw = new BufferedWriter(fw);

			// フィルタ後の波を全て書き出す
			wave_filtered.forEach(val -> {
				try {
					bw.write(val.toString());
					bw.newLine();
				}
				catch (IOException e) {
					System.out.println("入出力エラーです。");
					return;
				}
				return;
			});

			bw.close();
		}
		catch (IOException e) {
			System.out.println("入出力エラーです。");
			return;
		}
	}

	// 二つのstreamを合成する
	public static<A, B, C> Stream<C> zip(Stream<? extends A> a,
										 Stream<? extends B> b,
										 BiFunction<? super A, ? super B, ? extends C> zipper) {
		Objects.requireNonNull(zipper);
		Spliterator<? extends A> aSpliterator = Objects.requireNonNull(a).spliterator();
		Spliterator<? extends B> bSpliterator = Objects.requireNonNull(b).spliterator();
	
		int characteristics = aSpliterator.characteristics() & bSpliterator.characteristics() &
				~(Spliterator.DISTINCT | Spliterator.SORTED);
	
		long zipSize = ((characteristics & Spliterator.SIZED) != 0)
				? Math.min(aSpliterator.getExactSizeIfKnown(), bSpliterator.getExactSizeIfKnown())
				: -1;
	
		Iterator<A> aIterator = Spliterators.iterator(aSpliterator);
		Iterator<B> bIterator = Spliterators.iterator(bSpliterator);
		Iterator<C> cIterator = new Iterator<C>() {
			@Override
			public boolean hasNext() {
				return aIterator.hasNext() && bIterator.hasNext();
			}
	
			@Override
			public C next() {
				return zipper.apply(aIterator.next(), bIterator.next());
			}
		};
	
		Spliterator<C> split = Spliterators.spliterator(cIterator, zipSize, characteristics);
		return (a.isParallel() || b.isParallel())
			   ? StreamSupport.stream(split, true)
			   : StreamSupport.stream(split, false);
	}
}

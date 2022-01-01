import pathlib

import phlorest


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "bouckaert_et_al2018"

    def cmd_makecldf(self, args):
        self.init(args)
        args.writer.add_summary(
            self.raw_dir.read_tree('41559_2018_489_MOESM4_ESM.txt'),
            self.metadata,
            args.log)
        posterior = self.sample(
            self.remove_burnin(
                self.raw_dir.read('pny10.fixed.cov.ucln.bdsky.ba-sp.trees.gz'),
                1000),
            detranslate=True,
            as_nexus=True)
        args.writer.add_posterior(
            posterior.trees.trees,
            self.metadata,
            args.log)
        args.writer.add_data(
            phlorest.BeastFile(self.raw_dir / '41559_2018_489_MOESM3_ESM.xml'),
            self.characters,
            args.log)

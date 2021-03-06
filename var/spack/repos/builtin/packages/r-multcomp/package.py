##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class RMultcomp(Package):
    """Simultaneous tests and confidence intervals for general linear
    hypotheses in parametric models, including linear, generalized linear,
    linear mixed effects, and survival models. The package includes demos
    reproducing analyzes presented in the book "Multiple Comparisons Using R"
    (Bretz, Hothorn, Westfall, 2010, CRC Press)."""

    homepage = "http://multcomp.r-forge.r-project.org/"
    url      = "https://cran.r-project.org/src/contrib/multcomp_1.4-6.tar.gz"
    list_url = "https://cran.r-project.org/src/contrib/Archive/multcomp"

    version('1.4-6', 'f1353ede2ed78b23859a7f1f1f9ebe88')

    extends('R')

    depends_on('r-mvtnorm', type=nolink)
    depends_on('r-survival', type=nolink)
    depends_on('r-thdata', type=nolink)
    depends_on('r-sandwich', type=nolink)
    depends_on('r-codetools', type=nolink)

    def install(self, spec, prefix):
        R('CMD', 'INSTALL', '--library={0}'.format(self.module.r_lib_dir),
          self.stage.source_path)
